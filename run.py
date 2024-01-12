# Commands to load words from words_library
import random 
from words import word_library

# Function to get random word from Library
def get_word():
    word = random.choice(word_library)
    return word.lower()

incorrect_guesses = 0
letters_guessed = []
incorrect_guesses_allowed = len(cliffhanger_display)
word = random_word
letters_word = word
wrong_letters = []

print()
print("Welcome to the Cliffhanger word guessing game")
print("The word has {} letters".format(len(letters_word)))


# Function to show display of attempts
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

    for stage in stages:
        print(stage)

cliffhanger_display(1)