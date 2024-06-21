import os
import random

os.system('cls')

choices = {1: "Rock", 2: "Paper", 3: "Sissors"}

def showChoice(x):
    return choices.get(x)

player = 0

while player > 0 or player <= 3:
    playerChoice = input("Enter your choice:\n 1 for Rock\n 2 for Paper\n 3 for Sissors\n\n")
    try:
        player = int(playerChoice)
        break
    except:
        print("INVALID_CHCOICE_ENTERED")
        

computer = random.choice("123")
computer = int(computer)

print('\n' + "Player choice: " + showChoice(player))
print("Computer choice: " + showChoice(computer) + '\n')

if player == 1 and computer == 3:
    print('You Win!')
elif player == 2 and computer == 1:
    print('You Win!')
elif player == 3 and computer == 2:
    print('You Win!')
elif player == computer:
    print('Tie!')
else:
     print('You Lose')