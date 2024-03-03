"""
Categories Hangman
"""

import os
from words import sports
from words import vegetbales
from words import occupations


def clear():
    """
    Clears the screen.
    """
    os.system("clear")


def instructions():
    """
    Display the instructions menu to terrminal.
    """
    print("The goal of the game is simple:\n")
    print("Guess letters from the english alphabet")
    print("If your letter is in the word it's location(s) will be revealed")
    print("Be careful tho... If you guess incorrectly you will lose a life")
    print("Everytime you lose a life more of Hangman will be seen")
    print("If Hangman is fully revealed you have lost the game\n")
    print("Good Luck!")


def main_menu():
    """
    Displays sarting screen to the game.
    All other functions are executed from here.
    """
    print("Welcome to Categories Hangman\n")
    print("1. Play Hangman")
    print("2. Read Instructions\n")

    navigate_main = input("Enter your selection: ")

    while True:
        try:
            if navigate_main == "1":
                clear()
                # play()
                break
            elif navigate_main == "2":
                clear()
                instructions()
                break
            else:
                raise ValueError(
                    "Please enter 1 or 2"
                )
        except ValueError as e:
            clear()
            print(e)
            return main_menu()


main_menu()
