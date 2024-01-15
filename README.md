# CliffHanger - Word Guessing Game

CliffHanger is a text based Python terminal game. The program runs in Code Institutes mock terminal on Heroku.

CliffHanger is a new take on the popular Hangman game. 

The players incorrect guesses move the Cliffhanger stick-man closer to the edge of a cliff, with the Stickman taking an unlucky tumble if the player uses up all their attempts at guessing the word.

There is a vast library of words the program has access to, which gives the player a real challenge in solving. Over 170 words!!!

[View the live version of the game here. Enjoy!](https://cliff-hanger-69cb06fcdcfe.herokuapp.com/)

![Responsive Website]()

## How to play

If you are familiar with the word guessing game "Hangman" then you will get the gist of Cliffhanger.
If you have never played Hangman, please view the rules and concept of the game here.

When the game begins you will be informed of how many letters the word you need to guess contains.

You will then be asked to input a letter.

Upon the letter you input being correct, your correctly guessed letter will be shown and also at what point in the word your letter belongs.

If you guess an incorrect letter, the CliffHanger stick-man will move along the play area and your incorrect guess will be logged.

If you guess too many incorrect letters, the CliffHanger man will take tumble off the cliff.

On guessing the correct word, congratulations, you will be informed you have won the game.

After winning or losing you will be asked if you want to play the game again.

If you select "y" the game will start over and you can play a new game.

If you select "n" you will be shown a message "Thanks for playing" and the game will end.

## Features

### Current Features

- Words are selected from a large library, over 170 word options!

- Player is shown how many letters are in the word they need to guess.

- Correctly guessed letters are show on the word being guessed.

- Incorrect letters are stored and shown to the player, remaining amount of guesses allowed also shown to player.

- Input guesses are validated, if the player has already guessed the letter, they will be informed and asked to guess again.

- Upon reach the end of the game. After either a win or loss. The player will be asked if they want to play again. 
- If the player want to play again, the game will start again. 
- If the player doesn't want to play again the game will exit with a message, "Thanks for playing".

### Furtue Feature

Allow the play to select the difficulty of the game. 
With this suggestion:
- 6 attempt - Hard
- 8 attempts - Medium (current format)
- 10 attempts - Easy

## Data Model

The game harnesses the "random" module to select a word at random.

The words are stored in a library which are in their on .py file. This is to keep that data free from cluttering the main code and prevent the risk of misakes being made on main code if library is editied.

Visual reprisentation of an incorrect guess is used by having the stick-man shown and also have it move along the play area with each bad guess.
This is done by an if statement that prints the cliffhanger_display(+1) with each incorrect guess.

Game progress is stored and shown to the player.

Upon game outcome, the game loop is either restarted or exited depending on user input.

## Testing

### Bugs

- #### Solved Bugs

- #### Remaining Bugs

- Inconsistancy in uppercase input. Some uppercase letters are accepted but not all. 

### Validator Testing

## Deployment

## Credits