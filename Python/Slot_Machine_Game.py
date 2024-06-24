import random
import os

wallet = 5_000_000
MAX_LINES = 3
MIN_BET = 1

ROWS = 3
COLS = 3
symbols = {"💯": 2, "🎉": 4, "🚥": 6, "💩": 8}

def slot_machine_spin(rows, cols, symbols):
    allsymbols = []
    for symbol, symbols_count in symbols.items():
        for i in range(symbols_count):
            allsymbols.append(symbol)
    
    columns = []
    for i in range(cols):
        column = []
        current_symbols = allsymbols[:]
        for i in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    
    return columns

def printSlotMachine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row])
    print()

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines

def deposit(wallet):
    os.system('cls')
    while True:
        amount = input(f"Please enter the amount you want to deposit(Your wallet: ${wallet:,}):\n$")
        if amount.isdigit():
            amount = int(amount)
            if wallet >= amount:
                wallet -=  amount
                if amount > 0:
                    return amount, wallet
                else:
                    print("ERROR: Please enter an amount larger than 0")
            else:
                print(f"You don't have that kind of money, you have ${wallet:,} in your wallet")
        else:
            print("ERROR: The amount you want to deposit is invalid")

def get_number_of_lines():
    while True:
        lines = input(f"Please enter the amount of lines you want to bet on (1-{MAX_LINES}):\n")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("ERROR: Please enter a valid number of lines")
        else:
            print("ERROR: The amount of lines you want to bet on is invalid")
    os.system('cls')
    return lines

def get_bet(balance):
    while True:
        amount = input("Please enter the amount you want to bet on each line:\n$")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= balance:
                break
            else:
                print(f"ERROR: Please enter an amount larger than ${MIN_BET} and less than your balance ${balance:,}")
        else:
            print("ERROR: The amount you want to bet is invalid")
    os.system('cls')
    return amount

def play_again(balance, wallet):
    while True:
        inp = input("\nDo you want to play again? (y/n): ")
        inp = inp.lower()
        if inp != "y" and inp != "n":
            print("ERROR: Please try again")
            continue
        elif inp == "y":
            main(balance, wallet)
            break
        elif inp == "n":
            quit()

def main(balance, wallet):
    while True:
        os.system('cls')
        balance = balance
        lines = get_number_of_lines()
        bet = get_bet(balance)
        while True:
            total_bet = bet * lines
            if total_bet > balance:
                print(f"You don't have enough balance to bet that amount, your balance is ${balance:,}")
                U_inp = input("""
                    Enter 1 to re-deposit
                    Enter 2 to change the line amount
                    Enter 3 to change the bet amount
                    Or enter anything else to exit
                    """)
                if U_inp.isdigit():
                    os.system('cls')
                    U_inp = int(U_inp)
                    if U_inp == 1:
                        os.system('cls')
                        balance, wallet = deposit(balance, wallet) # type: ignore
                        continue
                    if U_inp == 2:
                        os.system('cls')
                        lines = get_number_of_lines()
                        continue
                    if U_inp == 3:
                        os.system('cls')
                        bet = get_bet(balance)
                        continue
                else:
                    os.system('cls')
                    quit()
            else:
                break
        print(f"You are betting ${bet:,} on {lines} lines, Total bet is equal to: ${total_bet:,}")
        balance -= total_bet
        slots = slot_machine_spin(ROWS, COLS, symbols)
        printSlotMachine(slots)
        winnings, winning_lines = check_winnings(slots, lines, bet, symbols)
        print(f"You won ${winnings:,}.")
        winning_lines = int(*winning_lines)
        if winning_lines >= 1:
            print("You won on lines:", winning_lines)
        balance += winnings
        print(f"Your current balance is ${balance:,}")
        print(f"You have ${wallet:,} left in your wallet")
        if wallet == 0 and balance == 0:
            print("You ran out of money because you played too much, now get out")
            break
        else:
            play_again(balance, wallet)
            break
    return 0

balance, wallet = deposit(wallet)
main(balance, wallet)
