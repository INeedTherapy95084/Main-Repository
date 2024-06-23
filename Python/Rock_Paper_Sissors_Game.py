import os
import random

os.system('cls')

def showChoice(x):
    choices = {1: "Rock", 2: "Paper", 3: "Sissors"}
    
    return choices.get(x)

def check_winner(player, computer):
    if player == 1 and computer == 3:
        print('You Win!\n')
    elif player == 2 and computer == 1:
        print('You Win!\n')
    elif player == 3 and computer == 2:
        print('You Win!\n')
    elif player == computer:
        print('Tie!\n')
    else:
        print('You Lose\n')

while True:
    player = 0

    while player > 0 or player <= 3 or player == "exit" or  player == "Exit":
        playerChoice = input("Enter your choice:\n 1 for Rock\n 2 for Paper\n 3 for Sissors\n\n")
        try:
            if player == "exit" or  player == "Exit":
                quit()
            player = int(playerChoice)
            break
        except:
            print("INVALID_CHCOICE_ENTERED")
            

    computer = int(random.choice("123"))

    print(f"\nPlayer choice: {showChoice(player)}")
    print(f"Computer choice: {showChoice(computer)} \n")

    check_winner(player, computer)