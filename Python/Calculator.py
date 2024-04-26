print("***************** CALCULATOR *****************\n")

while True:
    firstnum = input("Enter the first number: \n")
    try:
        firstnum = int(firstnum)
        break
    except:
        print("ERROR_INVALID_VALUE_\n")
        continue

while True:
    op = input("Enter an operator (+, -, *, /): \n")
    if op != '+' or op != '-' or op != '*' or op != '/':
        break
    else:
        print("ERROR_INVALID_VALUE_\n")
        continue
    
while True:
    secondnum = input("Enter the first number: \n")
    try:
        secondnum = int(firstnum)
        break
    except:
        print("ERROR_INVALID_VALUE_\n")
        continue

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
