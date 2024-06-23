import os

def get_num(no) -> int | str:
    while True:
        num = input(f"Enter the {no} number: \n")
        if num == 'quit' or num == 'Quit':
            return num
        try:
            num = int(num)
            return num
        except:
            print("ERROR_INVALID_VALUE_\n")
            continue

def Calculate(firstnum, op, secondnum) -> int:
    if op == '+':
        result = firstnum + secondnum
    elif op == '-':
        result = firstnum - secondnum
    elif op == '*':
        result = firstnum * secondnum
    elif op == '/':
            result = firstnum / secondnum
            
    return result

if __name__ == '__main__':
    
    os.system('cls')
    
    while True:
        print("\n***************** CALCULATOR *****************\n")

        firstnum = get_num("first")
        if firstnum == 'quit' or firstnum == 'Quit':
            break

        while True:
            op = input("Enter an operator (+, -, *, /): \n")
            if op == 'quit' or op == 'Quit':
                break
            elif op == '+' or op == '-' or op == '*' or op == '/':
                break
            else:
                print("ERROR_INVALID_VALUE_\n")
                continue
        if op == 'quit' or op == 'Quit':
            break
            
        while True:   
            secondnum = get_num("second")
            if secondnum == 0 and op == '/':
                print("\nERROR: Division by zero is not allowed.\n")
                continue
            elif secondnum == 'quit' or secondnum == 'Quit':
                    break
            break
        if secondnum == 'quit' or secondnum == 'Quit':
            break

        

        print("\nResult:", Calculate(firstnum, op, secondnum))

    print("\n**********************************************")