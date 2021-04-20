"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces.

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def pre_game():
    # Nice starting stuff like decorations and asking for a name
    print("\n└[∵┌]└[ ∵ ]┘[┐∵]┘\n")
    print("Hello, and welcome to the Number Guessing Game!")
    player_name = input("What's your name? ")
    print("Hiya {}, let's play!".format(player_name))


def start_round():
    print("----------START ROUND-------------")
    #mention the high score
    if high_score == 9999:
        print("There is no current high score. Claim it!")
    else:
        print("The current high score is {}.".format(high_score))

    # generate random number between 1 and 10
    answer = random.randint(1, 10)

    print("I am thinking of a number between 1 and 10...")

    # variables to store user's last guess and the number of attempts
    user_answer = 0
    guesses = 0

    while user_answer != answer:
        guesses += 1
        try:
            user_answer = int(input("Your guess please: "))
            if user_answer < 1 or user_answer > 10:
                raise ValueError
            elif user_answer < answer:
                print("It's higher. Try again!")
            else:
                print("It's lower. Try again!")

        except ValueError:
            print("That was not a valid guess, it must be an integer between 1 and 10...Try again!")

    print("You've got it! The answer was {}.".format(answer))
    print("It took you {} guesses.".format(guesses))
    print("----------END ROUND-------------")

    #update high score and return to update external high score variable
    if guesses < high_score:
        return guesses
    else:
        return high_score


def end_game():
    print("The best high score was {}.".format(high_score))
    print("Thanks for playing!")
    print("\n└[∵┌]└[ ∵ ]┘[┐∵]┘\n")


#External game variables
high_score = 9999

# Kick off the program by calling the start_game function.
pre_game()
high_score = start_round()
again = input("Do you want to play again?\n[Y] for yes, press any key to quit: ")
while again.upper() == "Y":
    high_score = start_round()
    again = input("Do you want to play again?\n[Y] for yes, press any key to quit: ")
end_game()
