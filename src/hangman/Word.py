#
# This script will access the words used by the GUI
#
import os

class Word:
    my_word = []
    path_to_project = os.path.abspath(os.path.join(__file__, "../../"))

    def __init__(self):
        self.my_word = []

    def get_word(self):
        return self.my_word

    def read_words_from_file(self):
        path_to_utils = self.path_to_project+"/utils"
        words = open(path_to_utils+'/words.txt', 'r')
        for word in words:
            word = word.split()
            print(word)
        self.my_word.extend(word)
        words.close()

    def get_my_words(self):
        return self.my_word


words = Word()
print(words.get_word())
