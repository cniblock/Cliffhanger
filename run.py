# Commands to link words from words_library
import random 
from words import word_library

# Function to get random word from Library
def get_word():
    word = random.choice(word_library)
    return word.lower()

# Stages of incorrect guesses
cliffhanger_display = ["""
           O
          \|/
          / \\
        ---------------------------¬
            """,
            """
                  O
                 \|/
                 / \\
        ---------------------------¬
            """,
            """
                      O
                     \|/
                     / \\
        ---------------------------¬
            """,
            """
                           O
                          \|/
                          / \\
        ---------------------------¬
            """,
            """
                                 O
                                \|/
                                / \\
        ---------------------------¬
            """,
            """
                                       \ O /    arrghh!!!
                                         |
                                        / \\
        ---------------------------¬
            """,
    ]

# Variables
word = get_word() 
incorrect_guesses = 0 
letters_guessed = []
incorrect_guesses_allowed = len(cliffhanger_display)
letters_word = list(word)
wrong_letters = []

# Initial print at start of the game
print()
print("Welcome to the Cliffhanger word guessing game\n")
print("The word has {} letters\n".format(len(letters_word)))

# While loop to check guesses / wrong guesses / ask for user input
while incorrect_guesses < incorrect_guesses_allowed:
    print()
    print("Incorrect letters guessed: ", end='')
    for letter in wrong_letters:
        print("{}, ".format(letter), end='')
    print()
    print("Guesses remaining: {}".format(incorrect_guesses_allowed - incorrect_guesses))
    letter_user = input
        ("Enter a letter: ")

# Valitate user input
    if len(letter_user) == 1 and letter_user.isalpha():
        break
    else:
        print("Error. Please enter a letter")

# Check if the letter has already been guessed
    while letter_user in letters_guessed or letter_user in wrong_letters:
        print()
        print("You have already guessed this letter. Please guess another letter")
        letter_user = input("Enter a letter: ")

# Check if the guessed letter is incorrect
    if letter_user not in letters_word:
        incorrect_guesses += 1
        wrong_letters.append(letter_user)

    print()
    print("Word: ", end="")

# For loop to add letter to guesses and check if letter is in word
    for letter in letters_word:
        if letter_user == letter:
            letters_guessed.append(letter_user)

    for letter in letters_word:
        if letter in letters_guessed:
            print(letter + " ", end="")
        else:
            print("_ ", end="")

    print()