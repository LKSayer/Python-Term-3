#options that player and opponent can decide

options = ["rock", "paper", "scissors"]

#points variable

Player_Lives = 3
#importing random features
 
import random

#making it so the code inside while loops when the player inputs an option

while Player_Lives > 0:

        #options that player can decide from, .lower is for if Uppercase words are inputted, .replace is if spaces are inputted

        user_action = input("Rock, Paper, or Scissors").lower().replace(" ", "")

        #point display

        print("Points:")
        print(Player_Lives)

        #Making AI Choose randomly

        random_choice = options[random.randint(0, 2)]

        #decide whether player wins, loses, or draws

        if user_action == random_choice:
            print("Draw")

        elif user_action == "rock" and random_choice == "paper":
            print("Paper: You Lose"); Player_Lives = Player_Lives - 1

        elif user_action == "rock" and random_choice == "scissors":
            print("Scissors: You Win"); Player_Lives = Player_Lives + 1

        elif user_action == "paper" and random_choice == "rock":
            print("Rock: You Win"); Player_Lives = Player_Lives + 1

        elif user_action == "paper" and random_choice == "scissors":
            print ("Scissors: You Lose"); Player_Lives = Player_Lives - 1

        elif user_action == "scissors" and random_choice == "rock":
            print("Rock: You Lose"); Player_Lives = Player_Lives - 1

        elif user_action == "scissors" and random_choice == "paper":
            print("Paper: You Win"); Player_Lives = Player_Lives + 1

        else:
            print("Enter a valid option")

#if Player_Lives reaches 0

else:
    print("Game Over")
    breakpoint
    



