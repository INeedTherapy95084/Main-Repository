import os
os.system('cls')

def is_convetable_to_float(num) -> bool:
    try:
        float(num)
        return True
    except:
        return False

def calculate(value, num1, num2) -> float:
    answer = 0
    
    if value == '+':
        answer = num1 + num2
    elif value == '-':
        answer = num1 - num2
    elif value == '*':
        answer = num1 * num2
    elif value == '/':
        if num2 == 0 and value == '/':
            print("\nERROR: Division by zero is not allowed.\n")
            quit()
        else:
            answer = num1 / num2
            
    return answer

print(f"{' CALCULATOR ':*^30}\n")

answer = None
iIndex = 0
sIndex = 1
inp = input('Enter an Equation:\n').split()

# 2 + 2 / 30 * 200 / 2 - 69

while True:
    if iIndex + 1 == len(inp):
        break
    elif is_convetable_to_float(inp[iIndex]) and is_convetable_to_float(inp[iIndex + 2]):
        if iIndex == 0:
            answer = calculate(inp[sIndex], float(inp[iIndex]), float(inp[iIndex + 2]))
        else:
            answer = calculate(inp[sIndex], answer, float(inp[iIndex + 2]))
        iIndex = iIndex + 2
        sIndex = sIndex + 2
    else:
        print('\nINVALID_INPUT_ERROR_1\n')
        inp = input('Enter an Equation:\n').split()
        symbol = inp
        answer = None
        iIndex = 0
        sIndex = 1
        continue
        
    
print(f"\nResult: {answer:,}")

print(f"\n{'*':*^30}\n")