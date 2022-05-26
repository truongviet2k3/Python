import random
import time
print("Welcome to RSL Game")
time.sleep(1)
name = input("Please input your name: ")

print(f"Hello {name} !")

player_guess = 0
computer_guess = 0

while player_guess != 'e':
    player_guess = input("Select scissor - s, rock - r, leaf - l, exit - e: ")
    while player_guess != 's'and player_guess != 'r' and player_guess != 'l' and player_guess != 'e':
        print("Your select is not accepted, please do it again!")
        player_guess = input("Select scissor - s, rock - r, leaf - l, exit - e: ")
    time.sleep(1)
    if player_guess == 'e':
        print("See you again!")
        exit()
    computer_guess = random.randint(1,3)
    if computer_guess == 1:
        computer_guess = 's'
    elif computer_guess == 2:
        computer_guess = 'r'
    elif computer_guess == 3:
        computer_guess = 'l'
    if computer_guess == player_guess:
        print(f"Draw!!! Computer guess: {computer_guess}")
    elif player_guess == 's':
        if computer_guess == 'r':
            print(f"You lose!!! Computer guess: {computer_guess}")
        else :
            print(f"You win!!! Computer guess: {computer_guess}")
    elif player_guess == 'r':
        if computer_guess == 's':
            print(f"You win!!! Computer guess: {computer_guess}")
        else:
            print(f"You lose!!! Computer guess: {computer_guess}")
    else: 
        if computer_guess == 's':
            print(f"You lose!!! Computer guess: {computer_guess}")
        else:
            print(f"You win!!! Computer guess: {computer_guess}")
