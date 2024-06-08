# Commands for random module and to link words from words_library
import random
from words import word_library


def get_word():
    """Function to get a random word from the library."""
    word = random.choice(word_library)
    return word.lower()


def display_cliffhanger(stage):
    """Function to display the current state of the cliffhanger."""
    cliffhanger_display = [
        """
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
    print(cliffhanger_display[stage])

def get_user_input(letters_guessed, wrong_letters):
    """Function to get a valid letter guess from the user."""
    while True:
        letter_user = input(" Enter a letter: ").lower()
        if len(letter_user) == 1 and letter_user.isalpha():
            if letter_user in letters_guessed or letter_user in wrong_letters:
                print(" You have already guessed this letter. Please guess another letter.")
            else:
                return letter_user
        else:
            print(" Invalid input. Please enter a single alphabet letter.")

def play_game():
    """Main function to play the game."""
    word = get_word()
    letters_word = list(word)
    letters_guessed = set()
    wrong_letters = set()
    incorrect_guesses = 0
    incorrect_guesses_allowed = 7

    print("\n Welcome to the CLIFFHANGER word guessing game\n")
    print(f" The word has {len(letters_word)} letters\n")

    while incorrect_guesses < incorrect_guesses_allowed:
        print(" Incorrect letters guessed: " + ", ".join(sorted(wrong_letters)))
        print(f" Guesses remaining: {incorrect_guesses_allowed - incorrect_guesses}")
        display_word(letters_word, letters_guessed)
        
        letter_user = get_user_input(letters_guessed, wrong_letters)

        if letter_user not in letters_word:
            incorrect_guesses += 1
            wrong_letters.add(letter_user)
        else:
            letters_guessed.add(letter_user)

        display_cliffhanger(incorrect_guesses)

        if set(letters_word) <= letters_guessed:
            print("\n CONGRATULATIONS! You won!")
            break

    if incorrect_guesses == incorrect_guesses_allowed:
        print("\n You lost! Better luck next time!")
        print(f" The correct word was: {word} \n")

            # Check if the guessed letter is incorrect
            if letter_user not in letters_word:
                incorrect_guesses += 1
                wrong_letters.append(letter_user)

            # Show correctly guessed letters
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

            
    