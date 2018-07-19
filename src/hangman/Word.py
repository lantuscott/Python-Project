#
# This script will access the words used by the GUI
#
import os

import random

acc = 0

class Word:

    """
    This class reads words from a txt file, creates a list of words and returns it
    """

    my_words = []  # Empty list to store the dictionary
    path_to_project = os.path.abspath(os.path.join(__file__, "../../"))  # This points to the final_project folder

    """
    This is the constructor of the class in which immediately calls the read_words_from_file definition when an object
    is created
    """

    def __init__(self):  # Constructor
        self.read_words_from_file()

    """
    This definition simply put, reads the file containing the words, puts them in a list called my_words
    """

    def read_words_from_file(self):
        path_to_utils = self.path_to_project+"/utils"
        words = open(path_to_utils+'/words.txt', 'r')
        self.my_words = words.read().split()
        words.close()

    """
    This definition returns the list of words
    """

    def get_my_words(self):
        return self.my_words

    '''
    A definition that calls the list (get_my_words()) picks a random item from the list and returns it
    self.method
    self.get_my_words()
    '''
    def random_word(self):      # selects a word from dictionary to
        #  start game
        ranWord = self.get_my_words()[random.randint(0, 99)]
        return ranWord

# Checks if letter is in mystery word and tracks number of guesses made and remaining
    def game_logic(self):
        acc = 0

        # User input to guess letter
        while True:
            guess = input("Enter a letter: ")
            guess = guess.lower()  # converts input to uppercase

            # Displays how many guesses you have made
            for attempts in range(1):
                attempts = 10
                print("Attempt #:", acc + 1)
                acc = acc + 1
                attempts = attempts - acc

                # Checks if input is valid (a single letter or if the input is same as length of the mystery word)
                if guess in "abcdefghijklmnopqrstuvwxyz":
                    if len(guess) == 0 or len(guess) == len(guess):
                        print("You guessed: ", guess)

                        #Checks if letter guessed is in mystery word
                        if guess in self.random_word():
                            print("you guessed it!")
                        # could also be word.find(guess), if true return whatever if false continue
                        else:
                            print("try again")
                            acc = acc + 1

                # If input is not valid prints error
                elif guess not in "abcdefghijklmnopqrstuvwxyz":
                    print("Input is not valid, Please enter a letter between 'a' and 'z': ")

                # Prints number of guesses remaining
                print("You have", attempts, "attempts remaining")
                if attempts <= 0:
                    print("Game Over!")

def main():
    wordObject = Word()

    print("Your word to guess has", len(wordObject.random_word()), "letters.")
    wordObject.game_logic()

if __name__ == '__main__':
    main()




