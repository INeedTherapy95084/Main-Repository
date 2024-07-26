import random
import os

KEY_OF_WORD: dict[str, list] | None = None # insert Key of word here


def create_key_to_code_decode() -> None:
    character_list = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[{]}|;:",<.>?`~あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをんがぎぐげごабвгдежзийклмнопрстуфхцчшщъыьэюяАБВГДЕЖЗИЙКЛМНОПРСТ')
    alphabet_code: dict[str, list] = {'a': [], 'b': [], 'c': [], 'd': [], 'e': [], 'f': [], 'g': [],
                          'h': [], 'i': [], 'j': [], 'k': [], 'l': [], 'm': [], 'n': [],
                          'o': [], 'p': [], 'q': [], 'r': [], 's': [], 't': [], 'u': [],
                          'v': [], 'w': [], 'x': [], 'y': [], 'z': [], ' ': [], 'A': [],
                          'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [], 'H': [],
                          'I': [], 'J': [], 'K': [], 'L': [], 'M': [], 'N': [], 'O': [],
                          'P': [], 'Q': [], 'R': [], 'S': [], 'T': [], 'U': [], 'V': [],
                          'W': [], 'X': [], 'Y': [], 'Z': [], '0': [], '1': [], '2': [],
                          '3': [], '4': [], '5': [], '6': [], '7': [], '8': [], '9': [],
                          '!': [], '"': [], '#': [], '$': [], '%': [], '&': [], "'": [],
                          '(': [], ')': [], '*': [], '+': [], ',': [], '-': [], '.': [],
                          '/': [], ':': [], ';': [], '<': [], '=': [], '>': [], '?': [],
                          '@': [], '[': [],  ']': [], '^': [], '_': [], '`': [],'{': [],
                          '|': [], '}': [], '~': [], '\\': [], '\n':[]}  

    random.shuffle(character_list)
    index = 0
    for alphabet in alphabet_code:
        for i in range(1,3):
            alphabet_code[alphabet].append(character_list[index])
            index += 1
    print(alphabet_code)


def coded_message(message: str) -> str:
    try:
        word_list: list = list(message)
        coded_word: str = ""
        for word in word_list:
            selected_key_word: str = random.choice(KEY_OF_WORD[word])
            coded_word += selected_key_word
            
        return coded_word
    except:
        print('\nERROR_\n')
        quit()

def decoded_message(message: str) -> str:
    try:
        coded_list: list = list(message)
        decoded_word: str = ""
        for coded_word in coded_list:
            for word in list(KEY_OF_WORD):
                if coded_word in KEY_OF_WORD[word]:
                    decoded_word += word
                    
        return decoded_word
    except:
        print('\nERROR_\n')
        quit()

def code_file(file_path: str) -> None:
    try:
        with open(file_path, encoding='utf-8') as file:
            txt_data: str = file.read()
            word_list: list = list(txt_data)
            coded_word: str = ""
        for word in word_list:
            selected_word = None
            selected_word = random.choice(KEY_OF_WORD[word])
            coded_word += selected_word
            
        with open(file_path, "w", encoding='utf-8') as write_code:
            write_code.write(coded_word)
        print(f"File name {file_path} has now been encrypted.")
    except:
        print('\nERROR_\n')
        quit()
    
def decode_file(file_path: str)-> None:
    try:
        with open(file_path, encoding='utf-8') as f:
            txt_data: str = f.read()
            txt_data = decoded_message(txt_data)
            decoded_word: str = txt_data
            
        with open(file_path, "w", encoding='utf-8') as write_code:
            write_code.write(decoded_word)
        print(f"File name {file_path} has now been decrypted.")
    except:
        print('\nERROR_\n')
        quit()

if __name__ == "__main__":
    os.system('cls')
    
    if KEY_OF_WORD == None:
        create_key_to_code_decode()
        print("\nSet this as 'KEY_OF_WORD' in the code to continue using this script.")
        quit()
    
    while True:
        choice: int | str = input("""What do you want to do?:
                        1. Encrypt a text that I input
                        2. Decrypt a text that I input
                        3. Encrypt a file (File Path required)
                        4. Decrypt a file (File Path required)\n\n""")
        if choice.isdigit():
            choice = int(choice)
            os.system('cls')
            if choice < 6 and choice > 0:
                if choice == 1:
                    message: str = input("Write the message you want to encrypt:\n")
                    encrypt_message: str = coded_message(message)
                    print (f"Encrypted message: {encrypt_message}")
                    break
                elif choice == 2:
                    message: str = input("Write the message you want to decrypt:\n")
                    decrypt_message: str = decoded_message(message)
                    print(f"Decrypted message: {decrypt_message}")
                    break
                elif choice == 3:
                    file_path: str = input("Enter the file path of the file you want to encrypt:\n")
                    os.system('cls')
                    code_file(file_path)
                    break
                elif choice == 4:
                    file_path: str = input("Enter the file path of the file you want to decrypt:\n")
                    os.system('cls')
                    decode_file(file_path)
                    break
                elif choice == 5:
                    print(create_key_to_code_decode())
                    break
            else:
                print("\nERROR_INVALID_INPUT_\n")
                continue
        else:
            print("\nERROR_INVALID_INPUT_\n")
            continue
