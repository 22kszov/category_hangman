"""
Categories Hangman
"""

import os
import random
import colorama
from colorama import Fore
from words import sports, vegetbales, occupations


colorama.init(autoreset=True)

# Graphics from stack overflow
# (https://stackoverflow.com/questions/37514165/python-need-to-display-graphic-for-hangman-game)
graphic = [
    """
            +-------+
            |
            |
            | 
            |
            |
         ==============
        """,
    """
            +-------+
            |       |
            |       O
            | 
            |
            |
         ==============
        """,
    """
            +-------+
            |       |
            |       O
            |       |
            |
            |
         ==============
        """,
    """
            +-------+
            |       |
            |       O
            |      /|
            |
            |
         ==============
        """,
    """
            +-------+
            |       |
            |       O
            |      /|\ 
            |
            |
         ==============
        """,
    """
            +-------+
            |       |
            |       O
            |      /|\ 
            |      /
            |
         ==============
        """,
    """
            +-------+
            |       |
            |       O
            |      /|\ 
            |      / \ 
            |
         ==============
        """]


def clear():
    """
    Clears the screen.
    """
    os.system("clear")


def restart():
    """
    Gives prompt to restart or quit game after win/loss
    """
    print("\n")
    print(f"{Fore.YELLOW}Would you like the play again?")
    print("\n")
    print(f"{Fore.BLUE}1. Yes")
    print(f"{Fore.BLUE}2. No")
    print("\n")

    restart_data = input(f"{Fore.YELLOW}Enter your selection: ")

    # Validates input and loops input box until valid data is input
    while True:
        try:
            if restart_data == "1":
                clear()
                main_menu()
                break
            elif restart_data == "2":
                clear()
                print(f"{Fore.YELLOW}Thanks for playing!")
                break
            else:
                raise ValueError(
                    f"{Fore.RED}Please enter 1 or 2"
                )
        except ValueError as e:
            clear()
            print(e)
            return restart_data


def choose_category():
    """
    Choose category.
    """
    print(f"{Fore.YELLOW}Select your category:\n")
    print(f"{Fore.BLUE}1. Sports")
    print(f"{Fore.BLUE}2. Vegetables")
    print(f"{Fore.BLUE}3. Occupations\n ")

    category_chosen = input(f"{Fore.YELLOW}Enter your selection: ")

    # Validates input and loops input box until valid data is input
    while True:
        try:
            if category_chosen == "1":
                clear()
                print(f"{Fore.GREEN}You have chosen Sports!")
                return "sport"
            elif category_chosen == "2":
                clear()
                print(f"{Fore.GREEN}You have chosen Vegetables!")
                return "veg"
            elif category_chosen == "3":
                clear()
                print(f"{Fore.GREEN}You have chosen Occupations!")
                return "job"
            else:
                raise ValueError(
                    f"{Fore.RED}Please enter 1, 2 or 3"
                )
        except ValueError as e:
            clear()
            print(e)
            return choose_category()


def hangman():
    """
    Runs main game.
    Choose a category.
    Choose a word.
    Play hangman.
    """
    lives = 7
    mistakes_made = 0
    letters_guessed = []
    wrong_letters = []

    category = choose_category()
    word = ""

    if category == "sport":
        word = random.choice(sports).upper()
    elif category == "veg":
        word = random.choice(vegetbales).upper()
    elif category == "job":
        word = random.choice(occupations).upper()

    word_letters = list(word)

    print("\n")
    print(f"{Fore.MAGENTA}--------------------------------------------------")
    print(f"{Fore.YELLOW}The word has {len(word)} letters!")
    print("\n")

    while lives > mistakes_made:
        print("Letters guessed: ", end="")
        for letter in wrong_letters:
            print(f"{letter}, ", end="")
        print("\n")
        print(f"Lives remaining: {lives - mistakes_made}")
        print("\n")
        user_letter = input(f"{Fore.YELLOW}Enter your guess: ").upper()

        while len(user_letter) != 1 or user_letter.isnumeric():
            print("\n")
            print(f"{Fore.RED}Please guess a single letter! Try again!")
            user_letter = input(f"{Fore.YELLOW}Enter your guess: ").upper()

        while user_letter in letters_guessed or user_letter in wrong_letters:
            print("\n")
            print(f"{Fore.RED}You have already guessed this letter.")
            user_letter = input(f"{Fore.YELLOW}Enter your guess: ").upper()
            while len(user_letter) != 1 or user_letter.isnumeric():
                print("\n")
                print(f"{Fore.RED}Please guess a single letter! Try again!")
                user_letter = input(f"{Fore.YELLOW}Enter your guess: ").upper()

        clear()

        if user_letter not in word_letters:
            mistakes_made += 1
            wrong_letters.append(user_letter)

        print("\n")
        print("Word: ", end="")

        for letter in word_letters:
            if user_letter == letter:
                letters_guessed.append(user_letter)
            if letter in letters_guessed:
                print(f"{letter} ", end="")
            else:
                print("_ ", end="")

        print("\n")
        if mistakes_made:
            print(graphic[mistakes_made - 1])
        print("\n")
        print(f"{Fore.MAGENTA}-----------------------------------------------")

        if len(letters_guessed) == len(word_letters):
            print("\n")
            print(f"{Fore.GREEN}You Win!")
            restart()
            break

    if mistakes_made == lives:
        print("\n")
        print(f"{Fore.RED}You Lose!")
        print(f"{Fore.RED}The word was {word}")
        restart()


def instructions():
    """
    Display the instructions menu to terrminal.
    """
    print(f"{Fore.GREEN}The goal of the game is simple:\n")
    print(f"{Fore.GREEN}Guess letters from the english alphabet")
    print(f"{Fore.GREEN}Be careful tho...")
    print(f"{Fore.GREEN}If you guess incorrectly you will lose a life")
    print(f"{Fore.GREEN}If Hangman is fully revealed you have lost the game\n")
    print(f"{Fore.GREEN}Good Luck!\n")
    print(f"{Fore.BLUE}1. Play Hangman")
    print(f"{Fore.BLUE}2. Exit Game\n")

    navigate_instructions = input(f"{Fore.YELLOW}Enter your selection: ")

    # Validates input and loops input box until valid data is input
    while True:
        try:
            if navigate_instructions == "1":
                clear()
                main_menu()
                break
            elif navigate_instructions == "2":
                clear()
                print(f"{Fore.YELLOW}Thanks for playing!")
                break
            else:
                raise ValueError(
                    f"{Fore.RED}Please enter 1 or 2"
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
    print(f"{Fore.YELLOW}Welcome to Categories Hangman\n")
    print(f"{Fore.BLUE}1. Play Hangman")
    print(f"{Fore.BLUE}2. Read Instructions\n")

    navigate_main = input(f"{Fore.YELLOW}Enter your selection: ")

    # Validates input and loops input box until valid data is input
    while True:
        try:
            if navigate_main == "1":
                clear()
                hangman()
                break
            elif navigate_main == "2":
                clear()
                instructions()
                break
            else:
                raise ValueError(
                    f"{Fore.RED}Please enter 1 or 2"
                )
        except ValueError as e:
            clear()
            print(e)
            return main_menu()


main_menu()
