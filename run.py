# Commands to link words from words_library
import random 
from words import word_library
play = True

# Function to get random word from Library
def get_word():
    word = random.choice(word_library)
    return word.lower()

# Stages of incorrect guesses
cliffhanger_display = ["""
           O     You got this!
          \\|/
          / \\
        ---------------------------¬
            """,
             """
                O     It's ok!
               \\|/
               / \\
        ---------------------------¬
            """,
            """
                   O     I believe in you!
                  \\|/
                  / \\
        ---------------------------¬
            """,
            """
                      O     you can do it!
                     \\|/
                     / \\
        ---------------------------¬
            """,
            """
                           O     oh dear!
                          \\|/
                          / \\
        ---------------------------¬
            """,
            """
                              O     I can see the edge!
                             \\|/
                             / \\
        ---------------------------¬
            """,
            """
                                  O     oh no!
                                 \\|/
                                 / \\
        ---------------------------¬
            """,
            """
                                       \\ O /     arrghh!!!
                                         |
                                        / \\
        ---------------------------¬
            """,
    ]
while play == True:
    # Variables
    word = get_word() 
    incorrect_guesses = 0 
    letters_guessed = []
    incorrect_guesses_allowed = len(cliffhanger_display)
    letters_word = list(word)
    wrong_letters = []

    # Initial print at the start of the game
    print()
    print(" Welcome to the CLIFFHANGER word guessing game\n")
    print(" The word has {} letters\n".format(len(letters_word)))

    # While loop to check guesses / wrong guesses / ask for user input
    while incorrect_guesses < incorrect_guesses_allowed:
        print(" Incorrect letters guessed: ", end='')
        for letter in wrong_letters:
            print("{}, ".format(letter), end='')
        print()
        print(" Guesses remaining: {}".format(incorrect_guesses_allowed - incorrect_guesses))
        letter_user = input(" Enter a letter: ")

        # Validate user input
        if len(letter_user) == 1 and letter_user.isalpha():
            # Check if the letter has already been guessed
            while letter_user in letters_guessed or letter_user in wrong_letters:
                print()
                print(" You have already guessed this letter. Please guess another letter.")
                letter_user = input(" Enter a letter: ")

            # Check if the guessed letter is incorrect
            if letter_user not in letters_word:
                incorrect_guesses += 1
                wrong_letters.append(letter_user)

            # Update the guessed letters
            print()
            print(" Word: ", end="")

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

            # Check guess to see if incorrect and print Cliffhanger man
            if incorrect_guesses:
                print(cliffhanger_display[incorrect_guesses - 1])
            print("___________________________________________")
            # Print game win
            if len(letters_guessed) == len(letters_word):
                print()
                print(" CONGRATULATIONS! You won!")
                play_again = input(" Would you like to play again? (y/n) ").upper()
                if play_again == "N":
                    print(" Thanks for playing")
                    play = False
                elif play_again == "Y":
                    word = get_word() 
                    incorrect_guesses = 0 
                    letters_guessed = []
                    incorrect_guesses_allowed = len(cliffhanger_display)
                    letters_word = list(word)
                    wrong_letters = []
    # Print loss of game
    if incorrect_guesses == incorrect_guesses_allowed:
        print()
        print(" You lost! Better luck next time!")
        print(" The correct word was: {} \n".format(word))
        play_again = input(" Would you like to play again? (y/n) ").upper()
        if play_again == "N":
                    print(" Thanks for playing")
                    play = False