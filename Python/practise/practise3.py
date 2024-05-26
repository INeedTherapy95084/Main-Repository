def comparenums(.):

while True:
    num1 = input("type the first number you want to compare:\n")
    try:
        num1 = int(num1)
        if num1 > 0:
            break
        else:
            continue
    except:
        continue
    
while True:
    num2 = input("type the second number you want to compare:\n")
    try:
        num2 = int(num2)
        if num2 > 0:
            break
        else:
            continue
    except:
        continue
    
print(comparenums(num1, num2))