#
# This script will access the words used by the GUI
#
import os


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


wordObject = Word()

for x in range(len(wordObject.get_my_words())):
    print(wordObject.get_my_words()[x])






