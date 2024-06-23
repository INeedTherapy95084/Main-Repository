import os
import random

os.system('cls')

def showChoice(x):
    choices = {1: "Rock", 2: "Paper", 3: "Sissors"}
    
    return choices.get(x)

score = 0

def check_winner(player, computer):
    if player == 1 and computer == 3:
        print('You Win!\n')
        win = True
        return win
    elif player == 2 and computer == 1:
        print('You Win!\n')
        win = True
        return win
    elif player == 3 and computer == 2:
        print('You Win!\n')
        win = True
        return win
    elif player == computer:
        print('Tie!\n')
    else:
        print('You Lose\n')

while True:
    player = 0

    while player > 0 or player <= 3 or player == "exit" or  player == "Exit":
        playerChoice = input("Enter Your Choice:\n 1 For Rock\n 2 For Paper\n 3 For Sissors\n\n")
        try:
            if player == "exit" or  player == "Exit":
                quit()
            player = int(playerChoice)
            break
        except:
            print("\nINVALID_CHCOICE_ENTERED\n")
            

    computer = int(random.choice("123"))

    print(f"\nPlayer Choice: {showChoice(player)}")
    print(f"Computer Choice: {showChoice(computer)} \n")

    check_winner(player, computer)
    print(f"Your Score: {score}\n")