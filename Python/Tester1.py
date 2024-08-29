import string
import random

KEY_TO_WORD = {'a': ['d'], 'b': ['q'], 'c': ['2'], 'd': ['0'], 'e': ['{'], 'f': [';'], 'g': ['w'], 'h': ['~'], 'i': ['/'], 'j': ['r'], 'k': ['!'], 'l': 
['v'], 'm': [')'], 'n': ['b'], 'o': ['*'], 'p': ['['], 'q': ['@'], 'r': ['W'], 's': ['R'], 't': [','], 'u': ['$'], 'v': ['h'], 'w': ['u'], 'x': ['i'], 'y': ['.'], 'z': ['l'], 'A': ['V'], 'B': ['B'], 'C': ['I'], 'D': ['/'], 'E': ['Y'], 'F': ['t'], 'G': ['j'], 'H': ['J'], 'I': 
['9'], 'J': ['('], 'K': ['g'], 'L': ['<'], 'M': ['Z'], 'N': ['y'], 'O': ['n'], 'P': ['G'], 'Q': ['P'], 'R': ['O'], 'S': ['8'], 'T': ['e'], 'U': ['3'], 'V': ['_'], 'W': ['&'], 'X': ['?'], 'Y': ['6'], 'Z': ['c'], '0': ['x'], '1': ['^'], '2': ['Q'], '3': ['/'], '4': ['D'], '5': 
['M'], '6': ['`'], '7': ['"'], '8': ['}'], '9': ['5'], '!': ['s'], '"': ['o'], '#': ['K'], '$': ['\\'], '%': ['1'], '&': ['F'], "'": ['E'], '(': ['-'], ')': ['T'], '*': ['%'], '+': ['a'], ',': [']'], '-': ['+'], '.': ['X'], '/': ['#'], ':': ['f'], ';': ['='], '<': [' '], '=': ['C'], '>': ['p'], '?': ['N'], '@': ['U'], '[': ['H'], '\\': ['z'], ']': ['>'], '^': ['L'], '_': ['7'], '`': ['A'], '{': ['m'], '|': ['k'], '}': ['|'], '~': ['S'], ' ': [':']}

def create_key_to_code() -> None:
    charecter_list = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&()*+,-./:;<=>?@[\]^_`{|}~// ')
    
    random.shuffle(charecter_list)
    
    charecters = string.ascii_letters + string.digits + string.punctuation + '//' + ' '
    alphabet_list = {charecter : [] for charecter in charecters}
    
    index = 0
    
    for alphabet in alphabet_list:
        alphabet_list[alphabet].append(charecter_list[index])
        index += 1
    print(alphabet_list)
    
def code_message(message: str) -> str:
    main_message = list(message)
    coded_message = ''
    
    for word in main_message:
        select_word = random.choice(KEY_TO_WORD[word])
        coded_message += select_word
    
    return coded_message

def decode_message(message: str) -> str:
    coded_message = list(message)
    decoded_message = ''
    
    for code_word in coded_message:
        for word in KEY_TO_WORD:
            if code_word in KEY_TO_WORD[word]:
                decoded_message += word
    
    return decoded_message
    
    
if __name__ == '__main__':
    create_key_to_code()
    print(code_message(input('De:\n')))
    print(decode_message(input('De:\n')))