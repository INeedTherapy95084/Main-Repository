import ollama
import os
import pyttsx3

def help() -> None:
    print("\n/bye           = exit the program\n"
            "/clear         = clear terminal, /clr\n"
            "/help          = keyboard shortcuts list, /?\n")
    
def ask(query: str) -> str | None:
    if query.lower() == '/help' or query.lower() == '/?':
        help() 
        return None
    if query.lower() == '/clear' or query.lower() == '/clr':
        os.system('cls')
        return None
    else:
        query = f'{query} - answer in fewer words if possible'
        response = ollama.chat(model='llama3.1:8b', messages=[
            {
                'role': 'user',
                'content': query,
            },
        ])
        response = response['message']['content'] # type: ignore

        return response


def answer(text_speach) -> None: 
    query: str = input('>>  ')
    
    if query.lower() == '/bye':
        print("Goodbye, see you later.")
        text_speach.say("Goodbye, see you later.")
        text_speach.runAndWait()
        os.system('cls')
        quit()
    answer: str | None = ask(query)
    print(answer, '\n')
    text_speach.say(answer)
    text_speach.runAndWait()
    
if __name__ == '__main__':
    
    os.system('cls')
    text_speach = pyttsx3.init()
    print("Hello, How may I assist you today?")
    text_speach.say("Hello, How may i assist you today?")
    text_speach.runAndWait()
    os.system('cls')
    
    while True:
        answer(text_speach)