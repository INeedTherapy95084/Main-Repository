import random
import string
import tkinter as tk
from tkinter import scrolledtext, messagebox, filedialog
import ast

KEY_OF_WORD = None

BG_COLOR = "#2B2B2B"
TEXT_COLOR = "#FFFFFF"
BUTTON_BG_COLOR = "#1f4c82"
BUTTON_FG_COLOR = "#FFFFFF"
ENTRY_BG_COLOR = "#1E1E1E"
ENTRY_FG_COLOR = "#FFFFFF"
FONT = "Cascadia Code font"
FONT_SIZE = 13

def create_key():
    global KEY_OF_WORD
    
    extra_characters = list('あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをんがぎぐげごабвгдежзийклмнопрстуфхцчшщъыьэюяАБВГДЕЖЗИЙКЛМНОПРСТ')
    
    characters = string.ascii_letters + string.digits + string.punctuation + ' ' + '\n' + ''.join(extra_characters)
    character_list = list(characters)
    random.shuffle(character_list)

    KEY_OF_WORD = {char: [character_list[i], character_list[i + len(characters) // 2]] for i, char in enumerate(characters) if i < len(character_list) // 2}

    key_status_label.config(text="Key Status: Key is SET", fg="#00FF00")
    set_key_button.config(text="Change Key", command=set_key)
    messagebox.showinfo("Key Created", "The key has been generated. You can now save it.")

def save_key():
    global KEY_OF_WORD
    if KEY_OF_WORD is None:
        messagebox.showwarning("Warning", "No key has been created yet.")
        return

    key_file_path = filedialog.asksaveasfilename(defaultextension=".txt", title="Save Key File", filetypes=[("Text Files", "*.txt")])
    if key_file_path:
        with open(key_file_path, 'w', encoding='utf-8') as key_file:
            key_file.write(str(KEY_OF_WORD))  

        messagebox.showinfo("Key Saved", f"The key has been saved to {key_file_path}.")

def load_key(file_path):
    global KEY_OF_WORD
    try:
        with open(file_path, 'r', encoding='utf-8') as key_file:
            key_data = key_file.read()
            new_key = ast.literal_eval(key_data) 

        if KEY_OF_WORD == new_key:
            messagebox.showinfo("Info", "The key is already set to this value. No changes made.")
            return

        KEY_OF_WORD = new_key
        key_status_label.config(text="Key Status: Key is SET", fg="green")
        set_key_button.config(text="Change Key", command=set_key)
        messagebox.showinfo("Key Loaded", "The key has been successfully loaded.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def set_key():
    file_path = filedialog.askopenfilename(
        title="Select Key File",
        filetypes=[("Text Files", "*.txt")]
    )
    if file_path:
        load_key(file_path)

def is_key_set():
    if KEY_OF_WORD is None:
        messagebox.showwarning("Warning", "Key is not set. Please set a key first.")
        return False
    return True

def coded_message(message: str) -> str:
    coded_word = ""
    for word in message:
        if word in KEY_OF_WORD:
            selected_key_word = KEY_OF_WORD[word][0]  
            coded_word += selected_key_word
        else:
            coded_word += word  
    return coded_word

def decoded_message(message: str) -> str:
    decoded_word = ""
    for coded_word in message:
        decoded_char = next((char for char, codes in KEY_OF_WORD.items() if codes[0] == coded_word), coded_word)
        decoded_word += decoded_char
    return decoded_word

def encrypt():
    if not is_key_set():
        return
    input_text = input_text_box.get("1.0", tk.END).strip()
    if not input_text:
        messagebox.showwarning("Input Error", "Please enter text to encrypt.")
        return
    encrypted_text = coded_message(input_text)
    output_text_box.delete("1.0", tk.END)
    output_text_box.insert(tk.END, encrypted_text)

def decrypt():
    if not is_key_set():
        return
    input_text = input_text_box.get("1.0", tk.END).strip()
    if not input_text:
        messagebox.showwarning("Input Error", "Please enter text to decrypt.")
        return
    decrypted_text = decoded_message(input_text)
    output_text_box.delete("1.0", tk.END)
    output_text_box.insert(tk.END, decrypted_text)

def encrypt_file():
    if not is_key_set():
        return
    file_path = filedialog.askopenfilename(title="Select File to Encrypt", filetypes=[("All Files", "*.*")])
    if file_path:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            encrypted_content = coded_message(content)

            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(encrypted_content)

            messagebox.showinfo("Success", f"File '{file_path}' has been encrypted.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

def decrypt_file():
    if not is_key_set():
        return
    file_path = filedialog.askopenfilename(title="Select File to Decrypt", filetypes=[("All Files", "*.*")])
    if file_path:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            decrypted_content = decoded_message(content)

            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(decrypted_content)

            messagebox.showinfo("Success", f"File '{file_path}' has been decrypted.")
        except Exception as e:
            messagebox.showerror("Error", str(e))


def clear_text():
    input_text_box.delete("1.0", tk.END)
    output_text_box.delete("1.0", tk.END)

root = tk.Tk()
root.title("Encrypter and Decrypter")
root.geometry("600x500")

root.config(bg=BG_COLOR)

button_frame = tk.Frame(root, bg=BG_COLOR)
button_frame.pack(pady=10)

create_key_button = tk.Button(button_frame, text="Create Key", command=create_key, bg=BUTTON_BG_COLOR, fg=BUTTON_FG_COLOR)
create_key_button.pack(side=tk.LEFT, padx=5)

save_key_button = tk.Button(button_frame, text="Save Key", command=save_key, bg=BUTTON_BG_COLOR, fg=BUTTON_FG_COLOR)
save_key_button.pack(side=tk.LEFT, padx=5)

set_key_button = tk.Button(button_frame, text="Set Key", command=set_key, bg=BUTTON_BG_COLOR, fg=BUTTON_FG_COLOR)
set_key_button.pack(side=tk.LEFT, padx=5)

key_status_label = tk.Label(root, text="Key Status: Key is NOT SET", fg="red", bg=BG_COLOR)
key_status_label.pack(pady=5)

input_label = tk.Label(root, text="Input Text:", fg=TEXT_COLOR, bg=BG_COLOR)
input_label.pack()

input_text_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=8, bg=ENTRY_BG_COLOR, fg=ENTRY_FG_COLOR, insertbackground=TEXT_COLOR, font=(FONT, FONT_SIZE))

input_text_box.pack(pady=10)

output_label = tk.Label(root, text="Output Text:", fg=TEXT_COLOR, bg=BG_COLOR)
output_label.pack()

output_text_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=8, bg=ENTRY_BG_COLOR, fg=ENTRY_FG_COLOR, insertbackground=TEXT_COLOR, font=(FONT, FONT_SIZE))
output_text_box.pack(pady=10)

button_frame2 = tk.Frame(root, bg=BG_COLOR)
button_frame2.pack(pady=5)

encrypt_button = tk.Button(button_frame2, text="Encrypt", command=encrypt, bg=BUTTON_BG_COLOR, fg=BUTTON_FG_COLOR)
encrypt_button.pack(side=tk.LEFT, padx=5)

decrypt_button = tk.Button(button_frame2, text="Decrypt", command=decrypt, bg=BUTTON_BG_COLOR, fg=BUTTON_FG_COLOR)
decrypt_button.pack(side=tk.LEFT, padx=5)

file_operations_frame = tk.Frame(root, bg=BG_COLOR)
file_operations_frame.pack(pady=10)

encrypt_file_button = tk.Button(file_operations_frame, text="Encrypt File", command=encrypt_file, bg=BUTTON_BG_COLOR, fg=BUTTON_FG_COLOR)
encrypt_file_button.pack(side=tk.LEFT, padx=5)

decrypt_file_button = tk.Button(file_operations_frame, text="Decrypt File", command=decrypt_file, bg=BUTTON_BG_COLOR, fg=BUTTON_FG_COLOR)
decrypt_file_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(root, text="Clear", command=clear_text, bg=BUTTON_BG_COLOR, fg=BUTTON_FG_COLOR)
clear_button.pack(pady=10)

root.mainloop()