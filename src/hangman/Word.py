#
# This script will access the words used by the GUI
#
import os

import random


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

    # def __init__(self):  # Constructor
    #     self.read_words_from_file()

    """
    This definition simply put, reads the file containing the words, puts them in a list called my_words
    """
    @staticmethod
    def read_words_from_file():
        path_to_utils = Word.path_to_project+"/utils"
        words = open(path_to_utils+'/words.txt', 'r')
        Word.my_words = words.read().split()
        words.close()

    '''
    A definition that calls the list (get_my_words()) picks a random item from the list and returns it
    self.method
    self.get_my_words()
    '''
    @staticmethod
    def random_word():      # selects a word from dictionary to
        #  start game
        ranWord = Word.my_words[random.randint(0, 99)]
        return ranWord


def main():
    Word.read_words_from_file()
    print(Word.random_word())

if __name__ == '__main__':
    main()




