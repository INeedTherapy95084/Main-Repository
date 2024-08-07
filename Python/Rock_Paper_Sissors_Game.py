import os
import random

def showChoice(x: int) -> str | None:
    choices: dict[int, str] = {1: "Rock", 2: "Paper", 3: "Sissors"}
    return choices.get(x)

def check_winner(player: int, computer: int) -> bool:
    if player == 1 and computer == 3:
        print('You Win!\n')
        return True
    elif player == 2 and computer == 1:
        print('You Win!\n')
        return True
    elif player == 3 and computer == 2:
        print('You Win!\n')
        return True
    elif player == computer:
        print('Tie!\n')
        return False
    else:
        print('You Lose\n')
        return False
    
score: int = 0

while True:
    os.system('cls')
    
    print(f"{" ROCK PAPER SISSORS ":*^40}\n")
    
    while True:
        playerChoice: str = input("Enter Your Choice:\n 1 For Rock\n 2 For Paper\n 3 For Sissors\n\n")

        if playerChoice == "1" or playerChoice == "2" or playerChoice == "3":
            player: int = int(playerChoice)
            break
        else:
            print("\nINVALID_INPUT_\n")
            

    computer: int = int(random.choice("123"))

    print(f"\nPlayer Choice: {showChoice(player)}")
    print(f"Computer Choice: {showChoice(computer)} \n")

    win: bool = check_winner(player, computer)
    
    if win == True:
        score += 1
    
    print(f"Your Score: {score}\n")
    
    while True:
        playAgain: str = input("\nDo you want to play again? (y/n):\n")
        
        if playAgain == "n" or  player == "N" or playAgain == "y" or  player == "Y":
            if playAgain == "n" or  player == "N":
                print(f"\n{"*":*^40}\n")
                quit()
            else:
                break
        else:
            print("\nINVALID_INPUT_\n")
            continue