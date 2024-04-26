import random
import os

os.system('cls')

rand_num = random.randint(1, 100)

guess = None
no_guess = 0

print("******* GUESSING THE NUMBER GAME *******\n")

while guess != rand_num:
    guess = input("Guess the number(1-100): \n")

    guess = int(guess)
    
    if guess < rand_num:
        print("Too low")
        no_guess = no_guess + 1
        continue

    if guess > rand_num:
        print("Too high")
        no_guess = no_guess + 1
        continue
    
print("\nCorrect! You guessed it in" , no_guess, "tries\n")

print("**************************************")
