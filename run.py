"""
Categories Hangman
"""

import os
import random
from words import sports
from words import vegetbales
from words import occupations


def clear():
    """
    Clears the screen.
    """
    os.system("clear")


def choose_category():
    """

    """
    print("Select your category:\n")
    print("1. Sports")
    print("2. Vegetables")
    print("3. Occupations\n ")

    category_chosen = input("Enter your selection: ")

    # Validates input and loops input box until valid data is input
    while True:
        try:
            if category_chosen == "1":
                clear()
                print("You have chosen Sports!")
                break
            elif category_chosen == "2":
                clear()
                print("You have chosen Vegetables!")
                break
            elif category_chosen == "3":
                clear()
                print("You have chosen Occupations!")
                break
            else:
                raise ValueError(
                    "Please enter 1, 2 or 3"
                )
        except ValueError as e:
            clear()
            print(e)
            return choose_category()


def play():
    """
    Runs main game.
    Choose a category.
    Play hangman.
    """
    choose_category()


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
    print("Good Luck!\n")
    print("1. Play Hangman")
    print("2. Exit Game\n")

    navigate_instructions = input("Enter your selection: ")

    # Validates input and loops input box until valid data is input
    while True:
        try:
            if navigate_instructions == "1":
                clear()
                main_menu()
                break
            elif navigate_instructions == "2":
                clear()
                print("Thanks for playing!")
                break
            else:
                raise ValueError(
                    "Please enter 1 or 2"
                )
        except ValueError as e:
            clear()
            print(e)
            return instructions()


def main_menu():
    """
    Displays sarting screen to the game.
    All other functions are executed from here.
    """
    print("Welcome to Categories Hangman\n")
    print("1. Play Hangman")
    print("2. Read Instructions\n")

    navigate_main = input("Enter your selection: ")

    # Validates input and loops input box until valid data is input
    while True:
        try:
            if navigate_main == "1":
                clear()
                play()
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
