a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9]

for num in a:
    for num2 in b:
        if num == num2:
            print("True")
            quit()
        elif num != a[-1]:
            continue
        else:
            print("False")
            quit()