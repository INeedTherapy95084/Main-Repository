import os
os.system('cls')

def result(firstnum, op, secondnum):
    if op == '+':
        result = firstnum + secondnum
    elif op == '-':
        result = firstnum - secondnum
    elif op == '*':
        result = firstnum * secondnum
    elif op == '/':
            result = firstnum / secondnum
            
    return result

while True:
    print("\n***************** CALCULATOR *****************\n")

    while True:
        firstnum = input("Enter the first number: \n")
        if firstnum == 'quit' or firstnum == 'Quit':
            break
        try:
            firstnum = int(firstnum)
            break
        except:
            print("ERROR_INVALID_VALUE_\n")
            continue
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
        secondnum = input("Enter the second number: \n")
        if secondnum == 'quit' or secondnum == 'Quit':
            break
        try:
            secondnum = int(secondnum)
            if secondnum == 0 and op == '/':
                print("\nERROR: Division by zero is not allowed.\n")
                continue
            else:
                break
        except:
            print("ERROR_INVALID_VALUE_\n")
            continue
    if secondnum == 'quit' or secondnum == 'Quit':
            break

    

    print("\nResult:", result(firstnum, op, secondnum))

print("\n**********************************************")
