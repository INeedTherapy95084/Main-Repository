import os

def get_num(no: float | str) -> float | str:
    while True:
        num = input(f"Enter the {no} number: \n")
        
        if num == 'quit' or num == 'Quit':
            return num
        try:
            num = float(num)
            return num
        except:
            print("ERROR_INVALID_VALUE_\n")
            continue

def Calculate(firstnum: float = 0, op: str = '+', secondnum: float = 0 ) -> float:
    result = 0
    
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
        print(f"\n{' CALCULATOR ':*^30}\n")

        num1: float | str  = get_num("first")
        
        if num1 == 'quit' or num1 == 'Quit':
            break

        while True:
            op: str = input("Enter an operator (+, -, *, /): \n")
            
            if op == 'quit' or op == 'Quit':
                break
            elif op == '+' or op == '-' or op == '*' or op == '/':
                break
            else:
                print("ERROR_INVALID_VALUE_\n")
                continue
        if op == 'quit' or op == 'Quit':
            break
              
        num2: float | str = get_num("second")
        
        if num2 == 0 and op == '/':
            print("\nERROR: Division by zero is not allowed.\n")
            continue
        elif num2 == 'quit' or num2 == 'Quit':
            break

        Result = Calculate(num1, op, num2)

        print(f"\n{Result = :,}")

    print(f"\n{'*':*^30}\n")