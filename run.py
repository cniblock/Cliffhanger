# Commands to load ranndom word from words_library
import random 
from words import word_library

# Function to get word from Library
def get_word():
    word = random.choice(word_library)
    return word.lower()

random_word = get_word()
print(random_word)