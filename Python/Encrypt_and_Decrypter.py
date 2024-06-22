import random
import os
import getpass

KEY_OF_WORD = {'a': ['w', 'ぬ'], 'b': ['#', '('], 'c': ['р', '5'], 'd': ['O', 'В'], 'e': ['m', 'う'], 'f': [')', 'у'], 'g': ['ち', 'z'],
               'h': ['П', 'I'], 'i': ['?', 'よ'], 'j': ['に', 'H'], 'k': ['е', 'С'], 'l': ['か', 'Г'], 'm': ['る', 'E'], 'n': ['B', 'ほ'],
               'o': ['н', 'も'], 'p': ['へ', 'ら'], 'q': ['>', 'i'], 'r': ['я', 'U'], 's': ['в', 'a'], 't': ['c', 'з'], 'u': ['З', 'м'],
               'v': ['э', '2'], 'w': ['1', '['], 'x': ['ы', 'й'], 'y': ['む', 'ご'], 'z': ['n', 'ん'], ' ': ['G', 'さ'], 'A': ['y', 'k'],
               'B': ['ぐ', 'と'], 'C': ['.', 'て'], 'D': ['а', 'ь'], 'E': ['X', 'g'], 'F': ['*', '0'], 'G': ['о', 'た'], 'H': ['D', 'こ'],
               'I': ['f', 'の'], 'J': ['$', 'Е'], 'K': ['r', '4'], 'L': ['M', 'P'], 'M': ['г', 'W'], 'N': ['u', 'М'], 'O': ['Л', 'は'],
               'P': ['ゆ', 'Ж'], 'Q': ['|', 'ч'], 'R': ['%', 'が'], 'S': ['8', 'К'], 'T': ['あ', 'ж'], 'U': ['ひ', 'Б'], 'V': ['6', '<'],
               'W': ['す', 'く'], 'X': ['げ', 'ъ'], 'Y': ['お', 'ц'], 'Z': ['ろ', 'ふ'], '0': ['Q', 'п'], '1': ['わ', '^'], '2': ['Н', 'き'],
               '3': ['り', 'え'], '4': ['み', 'щ'], '5': ['せ', 'J'], '6': ['х', 'Z'], '7': ['И', 'Т'], '8': ['A', 'б'], '9': ['3', 'K'],
               '!': ['ま', 'Y'], '"': [':', 'を'], '#': ['{', '&'], '$': ['S', 'め'], '%': ['!', 'N'], '&': ['x', ']'], "'": ['そ', 'な'],
               '(': ['О', 'R'], ')': ['れ', 'т'], '*': ['с', 'o'], '+': ['j', 'Й'], ',': ['F', 'к'], '-': ['д', ';'], '.': ['ф', 'け'],
               '/': ['p', '_'], ':': ['や', '`'], ';': ['e', 'l'], '<': ['ю', 'd'], '=': ['q', '"'], '>': ['~', '+'], '?': ['А', 's'],
               '@': [',', 'v'], '[': ['7', 'T'], ']': ['し', 'C'], '^': ['ш', 'h'], '_': ['Р', 'つ'], '`': ['=', 'ね'], '{': ['L', '-'],
               '|': ['ぎ', 'Д'], '}': ['и', 'V'], '~': ['t', '}'], '\\': ['b', '9'], '\n': ['い', 'л']}


def create_key_to_code_decode():
    character_list = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[{]}|;:",<.>?`~あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをんがぎぐげごабвгдежзийклмнопрстуфхцчшщъыьэюяАБВГДЕЖЗИЙКЛМНОПРСТ')
    alphabet_code = {'a': [], 'b': [], 'c': [], 'd': [], 'e': [], 'f': [], 'g': [],
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


def coded_message(message):
    try:
        word_list = list(message)
        coded_word = ""
        for word in word_list:
            selected_key_word = random.choice(KEY_OF_WORD[word])
            coded_word += selected_key_word
            
        return coded_word
    except:
        print('\nERROR_\n')
        quit()

def decoded_message(message):
    try:
        coded_list = list(message)
        decoded_word = ""
        for coded_word in coded_list:
            for word in list(KEY_OF_WORD):
                if coded_word in KEY_OF_WORD[word]:
                    decoded_word += word
                    
        return decoded_word
    except:
        print('\nERROR_\n')
        quit()

def code_file(file_path):
    try:
        with open(file_path, encoding='utf-8') as file:
            txt_data = file.read()
            word_list = list(txt_data)
            coded_word = ""
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
    
def decode_file(file_path):
    try:
        with open(file_path, encoding='utf-8') as f:
            txt_data = f.read()
            txt_data = decoded_message(txt_data)
            decoded_word = txt_data
            
        with open(file_path, "w", encoding='utf-8') as write_code:
            write_code.write(decoded_word)
        print(f"File name {file_path} has now been decrypted.")
    except:
        print('\nERROR_\n')
        quit()
    

def get_password(num):
    password = None
    with open(r"E:\vscode\passwords.txt", encoding='utf-8') as f:
        temp = f.read()
        temp = decoded_message(temp)
        temp = temp.split()
    if len(temp) >= 2:
        password = temp[num]

    return password


if __name__ == "__main__":
    
    os.system('cls')
    
    PASSWORD = get_password(11)
    
    while True:
        choice = input("""What do you want to do?:
                        1. Encrypt a text that I input
                        2. Decrypt a text that I input
                        3. Encrypt a file (Password required)
                        4. Decrypt a file (Password required)\n\n""")
        if choice.isdigit():
            choice = int(choice)
            os.system('cls')
            if choice < 6 and choice > 0:
                if choice == 1:
                    message = input("Write the message you want to encrypt:\n")
                    encrypt_message = coded_message(message)
                    print (f"Encrypted message: {encrypt_message}")
                    break
                elif choice == 2:
                    message = input("Write the message you want to decrypt:\n")
                    decrypt_message = decoded_message(message)
                    print(f"Decrypted message: {decrypt_message}")
                    break
                elif choice == 3:
                    entered_password = getpass.getpass("Enter password:\n")
                    if entered_password == PASSWORD:
                        os.system('cls')
                        file_path = input("Enter the file path of the file you want to encrypt:\n")
                        os.system('cls')
                        code_file(file_path)
                        break
                    else:
                        print("INVALID_PASSWORD_")
                        break
                elif choice == 4:
                    entered_password = getpass.getpass("Enter password:\n")
                    if entered_password == PASSWORD:
                        os.system('cls')
                        file_path = input("Enter the file path of the file you want to decrypt:\n")
                        os.system('cls')
                        decode_file(file_path)
                        break
                    else:
                        print("INVALID_PASSWORD_")
                        break
                elif choice == 5:
                    entered_password = getpass.getpass("Enter password:\n")
                    if entered_password == PASSWORD:
                        os.system('cls')
                        print(create_key_to_code_decode())
                        break
                    else:
                        print("INVALID_PASSWORD_")
                        break
            else:
                print("\nERROR_INVALID_INPUT_\n")
                continue
        else:
            print("\nERROR_INVALID_INPUT_\n")
            continue
