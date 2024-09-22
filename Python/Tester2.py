import random
import string
import tkinter as tk
from tkinter import scrolledtext, messagebox, filedialog

# Global variable for the key
KEY_OF_WORD = None

def create_key():
    global KEY_OF_WORD
    extra_characters = list('あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをんがぎぐげごабвгдежзийклмнопрстуфхцчшщъыьэюяАБВГДЕЖЗИЙКЛМНОПРСТ')
    
    characters = string.ascii_letters + string.digits + string.punctuation + ' ' + '\n' + ''.join(extra_characters)
    character_list = list(characters)
    random.shuffle(character_list)

    # Create a dictionary for the key
    KEY_OF_WORD = {char: character_list[i] for i, char in enumerate(characters) if i < len(character_list)}

    messagebox.showinfo("Key Created", "The key has been generated. You can now save it.")

def save_key():
    global KEY_OF_WORD
    if KEY_OF_WORD is None:
        messagebox.showwarning("Warning", "No key has been created yet.")
        return

    key_file_path = filedialog.asksaveasfilename(defaultextension=".txt", title="Save Key File", filetypes=[("Text Files", "*.txt")])
    if key_file_path:
        with open(key_file_path, 'w', encoding='utf-8') as key_file:
            for char, code in KEY_OF_WORD.items():
                key_file.write(f"{char}:{code}\n")

        messagebox.showinfo("Key Saved", f"The key has been saved to {key_file_path}.")

def load_key(file_path):
    global KEY_OF_WORD
    KEY_OF_WORD = {}
    try:
        with open(file_path, 'r', encoding='utf-8') as key_file:
            for line in key_file:
                line = line.strip()
                if line:  
                    parts = line.split(':', 1)  
                    if len(parts) == 2:  
                        char, code = parts[0].strip(), parts[1].strip()
                        KEY_OF_WORD[char] = code
                    else:
                        messagebox.showwarning("Warning", f"Skipping malformed line: {line}")
        messagebox.showinfo("Key Loaded", "The key has been successfully loaded.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def set_key():
    file_path = filedialog.askopenfilename(title="Select Key File", filetypes=[("Text Files", "*.txt")])
    if file_path:
        load_key(file_path)

def coded_message(message: str) -> str:
    coded_word = ""
    for word in message:
        if word in KEY_OF_WORD:
            selected_key_word = KEY_OF_WORD[word]
            coded_word += selected_key_word
        else:
            coded_word += word  
    return coded_word

def decoded_message(message: str) -> str:
    decoded_word = ""
    for coded_word in message:
        decoded_char = next((char for char, code in KEY_OF_WORD.items() if code == coded_word), coded_word)
        decoded_word += decoded_char
    return decoded_word

def encrypt():
    input_text = input_text_box.get("1.0", tk.END).strip()
    if not input_text:
        messagebox.showwarning("Input Error", "Please enter text to encrypt.")
        return
    encrypted_text = coded_message(input_text)
    output_text_box.delete("1.0", tk.END)
    output_text_box.insert(tk.END, encrypted_text)

def decrypt():
    input_text = input_text_box.get("1.0", tk.END).strip()
    if not input_text:
        messagebox.showwarning("Input Error", "Please enter text to decrypt.")
        return
    decrypted_text = decoded_message(input_text)
    output_text_box.delete("1.0", tk.END)
    output_text_box.insert(tk.END, decrypted_text)

def encrypt_file():
    file_path = filedialog.askopenfilename(title="Select File to Encrypt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            encrypted_content = coded_message(content)

            # Write back to the original file (in-place encryption)
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(encrypted_content)

            messagebox.showinfo("Success", f"File '{file_path}' has been encrypted.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

def decrypt_file():
    file_path = filedialog.askopenfilename(title="Select File to Decrypt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            decrypted_content = decoded_message(content)

            # Write back to the original file (in-place decryption)
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(decrypted_content)

            messagebox.showinfo("Success", f"File '{file_path}' has been decrypted.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

def clear_text():
    input_text_box.delete("1.0", tk.END)
    output_text_box.delete("1.0", tk.END)

# Create main window
root = tk.Tk()
root.title("Encrypter and Decrypter")
root.geometry("600x500")

# Create UI elements
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

create_key_button = tk.Button(button_frame, text="Create Key", command=create_key)
create_key_button.pack(side=tk.LEFT, padx=5)

save_key_button = tk.Button(button_frame, text="Save Key", command=save_key)
save_key_button.pack(side=tk.LEFT, padx=5)

set_key_button = tk.Button(button_frame, text="Set Key", command=set_key)
set_key_button.pack(side=tk.LEFT, padx=5)

input_label = tk.Label(root, text="Input Text:")
input_label.pack()

input_text_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=10)
input_text_box.pack(pady=10)

output_label = tk.Label(root, text="Output Text:")
output_label.pack()

output_text_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=10)
output_text_box.pack(pady=10)

# Create a frame for the buttons
button_frame2 = tk.Frame(root)
button_frame2.pack(pady=5)

encrypt_button = tk.Button(button_frame2, text="Encrypt", command=encrypt)
encrypt_button.pack(side=tk.LEFT, padx=5)

decrypt_button = tk.Button(button_frame2, text="Decrypt", command=decrypt)
decrypt_button.pack(side=tk.LEFT, padx=5)

# Create a frame for file operation buttons
file_operations_frame = tk.Frame(root)
file_operations_frame.pack(pady=10)

encrypt_file_button = tk.Button(file_operations_frame, text="Encrypt File", command=encrypt_file)
encrypt_file_button.pack(side=tk.LEFT, padx=5)

decrypt_file_button = tk.Button(file_operations_frame, text="Decrypt File", command=decrypt_file)
decrypt_file_button.pack(side=tk.LEFT, padx=5)

# Add clear button
clear_button = tk.Button(root, text="Clear", command=clear_text)
clear_button.pack(pady=10)

# Start the GUI loop
root.mainloop()