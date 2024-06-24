import os
import random

os.system('cls')

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
    
    player: int = 0

    while player > 0 or player <= 3 or player == "exit" or  player == "Exit":
        playerChoice: str = input("Enter Your Choice:\n 1 For Rock\n 2 For Paper\n 3 For Sissors\n\n")
        try:
            if player == "exit" or  player == "Exit":
                quit()
            player: int = int(playerChoice)
            break
        except:
            print("\nINVALID_CHCOICE_ENTERED\n")
            

    computer: int = int(random.choice("123"))

    print(f"\nPlayer Choice: {showChoice(player)}")
    print(f"Computer Choice: {showChoice(computer)} \n")

    win: bool = check_winner(player, computer)
    
    if win == True:
        score += 1
    
    print(f"Your Score: {score}\n")