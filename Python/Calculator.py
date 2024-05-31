import os
os.system('cls')

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
            break
        except:
            print("ERROR_INVALID_VALUE_\n")
            continue
    if secondnum == 'quit' or secondnum == 'Quit':
            break

    if op == '+':
        result = firstnum + secondnum
    elif op == '-':
        result = firstnum - secondnum
    elif op == '*':
        result = firstnum * secondnum
    elif op == '/':
        if secondnum == 0:
            print("ERROR: Division by zero is not allowed.")
        else:
            result = firstnum / secondnum

    print("\nResult:", result)

print("\n**********************************************")
