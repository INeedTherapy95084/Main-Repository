import tkinter as tk
from tkinter import scrolledtext, messagebox
from PIL import Image, ImageTk
import threading
import queue
import json
from vosk import Model, KaldiRecognizer
import pyaudio
import noisereduce as nr
import numpy as np
from scipy.io.wavfile import write
import ollama
import pyttsx3
import time

print("Loading application...")


# Initialization
engine = pyttsx3.init()
engine.setProperty('rate', 150)
model = Model(model_name="vosk-model-en-us-0.22")
recognizer = KaldiRecognizer(model, 16000)
recognizer.SetWords(True)
is_recording = False
audio_queue = queue.Queue()
audio_stream = None
audio_frames_list = []  
query = ""  
response = ""
AI_name = "AIVA"



def stop_recording():
    global is_recording, audio_stream
    mic_button.config(image=mic_off_photo) 
    is_recording = False
    if audio_stream:
        audio_stream.stop_stream()
        audio_stream.close()

    if audio_frames_list:
        save_audio("command.wav")


def toggle_recording():
    global is_recording

    if is_recording:
        stop_recording()
        status_label.config(text="Recording stopped.")
        return

    is_recording = True
    mic_button.config(image=mic_on_photo)  
    status_label.config(text="Listening...")
    
    audio_frames_list.clear()

    threading.Thread(target=record_speech).start()


def record_speech():
    global audio_stream

    try:
        p = pyaudio.PyAudio()

        audio_stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=4000)

        recognizer.AcceptWaveform(b"") 
        
        noise_data = audio_stream.read(4000, exception_on_overflow=False)
        noise_frames = np.frombuffer(noise_data, dtype=np.int16)
        
        while is_recording:
            data = audio_stream.read(4000, exception_on_overflow=False)
            audio_frames = np.frombuffer(data, dtype=np.int16)
            
            audio_frames_list.append(audio_frames)

            reduced_noise = nr.reduce_noise(y=audio_frames, y_noise=noise_frames, sr=16000)

            reduced_data = reduced_noise.astype(np.int16).tobytes()

            if recognizer.AcceptWaveform(reduced_data):
                result = recognizer.Result()
                text = json.loads(result).get("text", "")
                if text:
                    result_text.tag_delete("partial")
                    result_text.insert(tk.END, text + "\n")
            else:
                partial_result = recognizer.PartialResult()
        
        status_label.config(text="Recording finished.")
        time.sleep(5)
        status_label.config(text="Press the Mic button to start recording.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
    finally:
        stop_recording()


def save_audio(filename="command.wav"):

    audio_data = np.hstack(audio_frames_list)

    write(filename, 16000, audio_data.astype(np.int16))
    print(f"Audio saved to {filename}")


def input_query():
    global query
    global response
    
    status_label.config(text="Query submitted")

    all_text = result_text.get("1.0", tk.END).strip()

    last_line = all_text.splitlines()[-1]
    
    query = last_line

    if query.lower() in ["/clr", "/cls", "/clear"]:
        clear_text_box()
        status_label.config(text="Text box cleared.")
    elif query.lower() == "/bye":
        hi_and_bye('bye')
    elif query.lower() in ["/help", '/?']:
        result_text.insert(tk.END,"\n\n/bye                   = Exit the program\n"
            "/clear, /cls, /clr  = Clear terminal\n"
            "/help, /?             = Keyboard shortcuts list\n\n")
        result_text.yview_moveto(1.0)
    elif ["your creator", "your maker", "the person who made you", "your developer", "the person who developed you"] in query.lower():
        time.sleep(2)
        result_text.insert(tk.END,"\n\nShayan Afraz\n\n")
        result_text.yview_moveto(1.0)
        root.after(100, lambda: speak_text("Shayan Afraz"))
    elif "introduce yourself" in query.lower():
        time.sleep(2)
        result_text.insert(tk.END,"\n\nAIVA: Hello, My name is AIVA (AI Voice Assistant), Im a LLM (Large Language Model) made by Shayan Afraz,\n"
                           "I run fully without a Internet Connection and I serve many purposes, You can ask me anything and I'll try my best to answer them for You\n"
                           "Would You like to ask any questions?\n\n")
        result_text.yview_moveto(1.0)
        root.after(100, lambda: speak_text("Hello, My name is Aiva, Im a Large Language Model made by Shayan Afraz, I run fully without a Internet Connection and I serve many purposes, You can ask me anything and I'll try my best to answer them for You, Would You like to ask any questions?"))
    else:  
        status_label.config(text="Loading response...")
        response = ask_ollama(query)
        result_text.insert(tk.END, f"\n\n {AI_name}:  {response}\n\n")
        result_text.yview_moveto(1.0)
        root.after(100, lambda: speak_text(response))
    
    status_label.config(text="Press the Mic button to start recording.")
        
        
def ask_ollama(query):
    query = f'{query} - answer in fewer words if possible'
    response = ollama.chat(model='llama3.1:8b', messages=[{'role': 'user', 'content': query}])
    response = response['message']['content']

    return response


def hi_and_bye(text):
    global AI_name
    if text == 'hi':
        result_text.insert(tk.END, f"{AI_name}: Hello, How may I assist you today? Type (/help) or (/?) to get further assistance\n\n")
        speak_text("Hello, How may I assist you today?")
    else:
        result_text.insert(tk.END, f"\n\n{AI_name}: Goodbye, See you later!\n\n")
        result_text.yview_moveto(1.0)
        speak_text("Goodbye, See you later!")
        root.after(2000, quit)  


def speak_text(text):
    engine.say(text)
    engine.runAndWait()


def clear_text_box():
    result_text.delete("1.0", tk.END) 


root = tk.Tk()
root.title(f"AIVoiceAssistant - {AI_name}")
root.geometry("800x800")

root.configure(bg="#C0C0C0") 

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

result_text = scrolledtext.ScrolledText(
    root, wrap=tk.WORD, width=100, height=20, font=("MS Sans Serif", 16),
    bg="black", fg="#39ff14", insertbackground="black", bd=2, relief="sunken"
)
result_text.grid(column=0, row=0, padx=20, pady=20, columnspan=3, sticky="nsew")

ask_button = tk.Button(root, text="Enter", font=("MS Sans Serif", 12), command=input_query, relief="raised", bd=2, bg="#C0C0C0")
ask_button.grid(column=1, row=2, padx=10, pady=10, sticky="n")

status_label = tk.Label(root, text="Press the Mic button to start recording.", font=("MS Sans Serif", 12),
                        bg="#f0f0f0", fg="black", relief="sunken", bd=2)
status_label.grid(column=0, row=3, padx=10, pady=10, columnspan=3, sticky="n")

mic_off_photo = ImageTk.PhotoImage(Image.open("mic_off.png").resize((50, 50)))
mic_on_photo = ImageTk.PhotoImage(Image.open("mic_on.png").resize((50, 50)))

mic_button = tk.Button(root, image=mic_off_photo, command=toggle_recording, relief="raised", bd=2)
mic_button.grid(column=1, row=4, padx=10, pady=10, sticky="n")

hi_and_bye('hi')

root.mainloop()
