from instagrapi import Client
import os
import getpass
import time
os.system('cls')

file_path = r"E:\vscode\Python\passwords.txt"

def decode_password(file_data):
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
    
    coded_list = list(file_data)
    decoded_word = ""
    for coded_word in coded_list:
        for word in list(KEY_OF_WORD):
            if coded_word in KEY_OF_WORD[word]:
                decoded_word += word

    return decoded_word
    
def get_password():
    password = None
    with open(file_path, encoding='utf-8') as f:
        temp = f.read()
        temp = decode_password(temp)
        temp = temp.split()
    if len(temp) >= 2:
        password = temp[2]

    return password

temp = get_password()
PASSWORD = temp

inp = input("Enter File Password:\n")

os.system('cls')

if inp == PASSWORD :
    inp = input("!WARNING!: Over excicuting this code might result in account termination, do you still wish to proceed? (y/n): ")
    inp = inp.lower()
    os.system('cls')
    if inp == 'y':
        inp = input("Do you want to use the defalt login information?(y/n): ")
        inp = inp.lower()
        os.system('cls')
        if inp == 'y':
            with open(file_path, encoding='utf-8') as f:
                temp = f.read()
                temp = decode_password(temp)
                temp = temp.split()
            if len(temp) >= 3:
                ACCOUNT_PASSWORD = temp[2]
            else:
                print("ERROR_COULD_NOT_FIND_PASSWORD_")
                
            ACCOUNT_USERNAME = '_i_need_therapy_2284'
        else:
            ACCOUNT_USERNAME = input("Enter your IG username:\n")
            os.system('cls')
            ACCOUNT_PASSWORD = getpass.getpass("Enter your password:\n")
            os.system('cls')
        
        inp = input("Are you sure that you want to exicute this code?(y/n): ")
        inp = inp.lower()
        os.system('cls')
        
        if inp == 'y': 
            
            inp = input("Are you SHUREEE that you want to exicute this code?(y/n): ")
            inp = inp.lower()
            os.system('cls')
        
            if inp == 'y':
                
                inp = input("Are you ABSOLUTELY SHUREEE that you want to exicute this code?!(y/n): ")
                inp = inp.lower()
                os.system('cls')
                
                if inp == 'y':
                    
                    inp = input("ARE YOU ABSOLUTELY AND WITH OUT A DOUBT SHUREEE THAT, YOU. WANT. TO. EXICUTE. THIS. CODE?!?!(y/n): ")
                    inp = inp.lower()
                    os.system('cls')
        
                    if inp == 'y':
                    
                        print("FINEE STUIT YOURSELF, DONT BLAME ME IF YOUR ACCOUNT GETS BANNED")
                        print("\nLOADING YOUR GODDAMN SCRIPT YOU STUBBORN-USER...")
                        time.sleep(5)
                        os.system('cls')
                        cl = Client()
                        cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)

                        followers = cl.user_followers(cl.user_id)
                        for user_id in followers.keys():
                            user_info = cl.user_info(52932375530)
                            print(user_info)



                        # cl.direct_send('How are you?', user_ids=[])  
                        # print('program ended sucsessfully')