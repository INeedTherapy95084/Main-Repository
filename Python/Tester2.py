import speech_recognition as sr
import pyttsx3
import wikipedia
import sqlite3
import datetime
import time
import threading
from transformers import pipeline

# Initialize text-to-speech
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Initialize SQLite database
def init_db():
    with sqlite3.connect('events.db') as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS events
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      title TEXT NOT NULL,
                      start TEXT NOT NULL,
                      end TEXT,
                      description TEXT,
                      reminder_minutes INTEGER)''')
        conn.commit()

init_db()

# Parse date and time
def parse_datetime(date_str, time_str):
    try:
        today = datetime.date.today()
        if date_str.lower() == "today":
            date = today
        elif date_str.lower() == "tomorrow":
            date = today + datetime.timedelta(days=1)
        else:
            for fmt in ["%B %d %Y", "%B %d", "%d %B %Y", "%d %B"]:
                try:
                    date = datetime.datetime.strptime(date_str, fmt).date()
                    break
                except ValueError:
                    continue
            else:
                date = today
        for fmt in ["%I %p", "%I:%M %p", "%H:%M"]:
            try:
                time_obj = datetime.datetime.strptime(time_str, fmt).time()
                break
            except ValueError:
                continue
            else:
                time_obj = datetime.time(0, 0)
        return datetime.datetime.combine(date, time_obj).isoformat()
    except:
        speak("Sorry, I couldn't parse the date or time.")
        return None

# Calendar functions
def add_event(title, start, end=None, description="", reminder_minutes=0):
    with sqlite3.connect('events.db') as conn:
        c = conn.cursor()
        c.execute('INSERT INTO events (title, start, end, description, reminder_minutes) VALUES (?, ?, ?, ?, ?)',
                  (title, start, end, description, reminder_minutes))
        conn.commit()
    speak(f"Event {title} added successfully.")

def list_events():
    with sqlite3.connect('events.db') as conn:
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        c.execute('SELECT * FROM events')
        events = c.fetchall()
    if not events:
        speak("You have no events scheduled.")
        return
    for event in events:
        start = datetime.datetime.fromisoformat(event['start'])
        speak(f"Event: {event['title']} on {start.strftime('%B %d at %I:%M %p')}")

def delete_event(title):
    with sqlite3.connect('events.db') as conn:
        c = conn.cursor()
        c.execute('DELETE FROM events WHERE title = ?', (title,))
        conn.commit()
        if c.rowcount > 0:
            speak(f"Event {title} deleted.")
        else:
            speak(f"No event found with title {title}.")

def reminder_thread():
    while True:
        with sqlite3.connect('events.db') as conn:
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute('SELECT * FROM events')
            events = c.fetchall()
        now = datetime.datetime.now()
        for event in events:
            start = datetime.datetime.fromisoformat(event['start'])
            reminder_time = start - datetime.timedelta(minutes=event['reminder_minutes'])
            if reminder_time <= now < start:
                speak(f"Reminder: {event['title']} starts at {start.strftime('%I:%M %p')}.")
                c.execute('UPDATE events SET reminder_minutes = 0 WHERE id = ?', (event['id'],))
                conn.commit()
        time.sleep(60)

def start_reminders():
    threading.Thread(target=reminder_thread, daemon=True).start()

def handle_calendar_command(command):
    command = command.lower().strip()
    if command.endswith('.'):
        command = command[:-1]
    if "add event" in command:
        try:
            parts = command.split("add event")[1].strip().split(" on ")
            title = parts[0].strip()
            date_time = parts[1].split(" at ")
            date_str = date_time[0].strip()
            time_str = date_time[1].strip()
            start = parse_datetime(date_str, time_str)
            if start:
                add_event(title, start, reminder_minutes=15)
        except:
            speak("Please specify the event title, date, and time clearly.")
    elif "show my events" in command:
        list_events()
    elif "delete event" in command:
        try:
            title = command.split("delete event")[1].strip()
            delete_event(title)
        except:
            speak("Please specify the event title to delete.")
    else:
        speak("Unknown calendar command.")

# Initialize the conversational model (runs locally, no API key needed)
chatbot = pipeline("text-generation", model="distilgpt2")

def chat_response(prompt):
    response = chatbot(prompt, max_length=50, num_return_sequences=1)[0]['generated_text']
    return response

# Main command processor
def process_command(command):
    command = command.lower().strip()
    if command.endswith('.'):
        command = command[:-1]
    if "wikipedia" in command:
        query = command.replace("wikipedia", "").strip()
        try:
            result = wikipedia.summary(query, sentences=2)
            speak(result)
        except:
            speak("Sorry, I couldn't find that on Wikipedia.")
    elif "calendar" in command or "event" in command:
        handle_calendar_command(command)
    elif "chat" in command or "ask" in command:
        query = command.replace("chat", "").replace("ask", "").strip()
        if query:
            response = chat_response(query)
            speak(response)
    else:
        speak("I don't understand that command.")

# Voice loop
def voice_listener():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        speak("Listening for commands. Say 'chat', 'ask', 'wikipedia', or 'calendar' to start.")
        while True:
            try:
                audio = recognizer.listen(source, timeout=5)
                command = recognizer.recognize_google(audio)
                print(f"Recognized: {command}")
                process_command(command)
            except sr.WaitTimeoutError:
                continue
            except sr.UnknownValueError:
                speak("Sorry, I didn't understand that.")
            except sr.RequestError:
                speak("Speech recognition service is unavailable.")
            except KeyboardInterrupt:
                speak("Shutting down.")
                break

if __name__ == "__main__":
    start_reminders()
    voice_listener()