from instagrapi import Client
import os
import getpass
import time
os.system('cls')

file_path = r"E:\vscode\Python\passwords.txt"

def decode_password(file_data):
    KEY_OF_WORD = {'a': ['S', 'ヒ'], 'b': ['ぺ', ':'], 'c': ['B', 'サ'], 'd': ['れ', 'ぶ'], 'e': ['ら', 'K'], 'f': ['g', 'や'], 'g': ['ナ', '7'],
                   'h': ['テ', 'せ'], 'i': ['エ', 'イ'], 'j': ['き', 'ヌ'], 'k': ['n', 'ば'], 'l': ['?', 'の'], 'm': ['っ', 'J'], 'n': ['q', 'k'],
                   'o': ['よ', '`'], 'p': ['シ', 'し'], 'q': ['3', 'ふ'], 'r': ['り', 'づ'], 's': ['!', 'T'], 't': ['わ', 'タ'], 'u': ['@', ')'],
                   'v': ['ぱ', '4'], 'w': ['5', '8'], 'x': ['べ', 'Y'], 'y': ['2', 'ぐ'], 'z': ['"', 'u'], ' ': ['む', 'a'], 'A': ['ゅ', 'あ'],
                   'B': ['で', 'Q'], 'C': ['な', 's'], 'D': ['V', 'ざ'], 'E': ['ぼ', 'O'], 'F': ['~', 'じ'], 'G': ['x', '='], 'H': ['0', 'C'],
                   'I': ['Z', 'ま'], 'J': ['け', '{'], 'K': ['U', 'ぜ'], 'L': ['G', 'キ'], 'M': ['す', 'か'], 'N': ['P', 'ソ'], 'O': ['セ', '-'],
                   'P': ['は', '>'], 'Q': ['%', 'v'], 'R': ['b', 'E'], 'S': ['ひ', ';'], 'T': ['l', 'ゃ'], 'U': ['y', 'ぷ'], 'V': ['お', 'ぞ'],
                   'W': ['N', '^'], 'X': ['げ', '&'], 'Y': ['つ', '|'], 'Z': ['F', 'だ'], '0': ['m', 'が'], '1': ['_', 'A'], '2': ['ぢ', 'え'],
                   '3': ['び', 'ウ'], '4': ['ぴ', 'め'], '5': [',', '$'], '6': ['t', 'ツ'], '7': ['}', 'ネ'], '8': ['D', '9'], '9': ['R', 'H'],
                   '!': ['み', 'く'], '"': ['ぬ', 'い'], '#': ['M', '1'], '$': ['ん', 'ね'], '%': ['f', 'z'], '&': ['<', 'ハ'], "'": ['さ', 'd'],
                   '(': ['る', 'ク'], ')': ['こ', 'ょ'], '*': ['X', 'を'], '+': ['に', 'w'], ',': ['ろ', '6'], '-': ['ニ', 'ノ'], '.': ['そ', '('],
                   '/': ['[', 'h'], ':': ['コ', 'ご'], ';': ['*', 'e'], '<': ['ス', 'カ'], '=': ['チ', 'ぽ'], '>': ['.', '#'], '?': ['c', 'L'],
                   '@': [']', 'ほ'], '[': ['I', 'へ'], ']': ['i', 'ゆ'], '^': ['ち', 'ど'], '_': ['ト', 'ア'], '`': ['o', 'と'], '{': ['ず', 'た'],
                   '|': ['+', 'オ'], '}': ['j', 'う'], '~': ['も', 'ぎ'], '\\': ['p', 'r']}
    
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