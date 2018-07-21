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
    attempt_number = 1

    """
    This is the constructor of the class in which immediately calls the read_words_from_file definition when an object
    is created
    """

    def __init__(self):  # Constructor
        self.read_words_from_file()

    """
    This definition simply put, reads the file containing the words, puts them in a list called my_words
    """

    def game_difficulty(self):
        return input("What difficulty do you want? Easy=e, Medium=m, Hard=h: ")

    def read_words_from_file(self):
        path_to_utils = self.path_to_project + "/utils"
        difficulty = self.game_difficulty()
        if difficulty == "e":
            words = open(path_to_utils + '/easy_words.txt', 'r')
            self.my_words = words.read().split()
        elif difficulty == "m":
            words = open(path_to_utils + '/medium_words.txt', 'r')
            self.my_words = words.read().split()
        elif difficulty == "h":
            words = open(path_to_utils + '/hard_words.txt', 'r')
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

    def random_word(self):  # selects a word from dictionary to
        #  start game
        ranWord = self.get_my_words()[random.randint(0, 99)]
        return ranWord

    # Checks if letter is in mystery word and tracks number of guesses made and remaining
    def game_logic(self):
        from src.hangman import Drawer
        gui = Drawer.Drawer()
        gui.game_screen()
        original_word_to_guess = self.random_word()
        mystery_word = self.mystery_word(original_word_to_guess)
        acc = 0
        guessed_letters = ''
        progress = ''
        temp = ""
        objectList = [gui]
        methodList = ['draw_base2()']
        remaining_letters = original_word_to_guess
        word_to_list = list(mystery_word)
        print("The words is :", original_word_to_guess)
        print('----------------------------------------------------')
        # User input to guess letter
        while True:
            print("Starred word: ", temp)
            guess = input("Enter a letter: ")
            guess = guess.lower()  # converts input to uppercase

            # Displays how many guesses you have made
            for attempts in range(1):
                attempts = 10
                acc += 1
                word_to_display = original_word_to_guess;
                print("Attempt #:", acc)
                attempts = attempts - acc
                # Checks if input is valid (a single letter or if the input is same as length of the mystery word)
                if guess in "abcdefghijklmnopqrstuvwxyz":
                    if len(guess) == 1:
                        progress += guess
                        # print("You guessed: ", guess)
                        if guess in remaining_letters:
                            remaining_letters = remaining_letters.replace(guess, '')
                            guessed_position = word_to_display.index(guess)
                            word_to_list[guessed_position] = guess
                            temp = "".join(word_to_list)
                            print("you guessed one letter!, remaining letters to be guessed: ", remaining_letters)
                        else:  # Here call the Turtle and create a figure every time a user misses
                            gui.method_factory(self.attempt_number)
                            self.attempt_number += 1
                            print("try again, attempsts -> ", attempts, " attempt_number -> ", self.attempt_number)
                # If input is not valid prints error
                elif guess not in "abcdefghijklmnopqrstuvwxyz":
                    print("Input is not valid, Please enter a letter between 'a' and 'z': ")

                guessed_letters += ' ' + guess
                print("Letters you have tried: ", guessed_letters)

                # When you guess the word, it will compare it with your progress, if it's a match the user wins
                if remaining_letters == "" and attempts > 0:
                    print("You guessed the word! HOORAY!!!", self.attempt_number)
                    gui.you_won()
                    pass
                elif attempts == 0 or self.attempt_number == 10:  # if attempts reach out the max, the user loses
                    print("Game Over!", self.attempt_number)
                    pass  # I use this to exit the While loop
                # Prints number of guesses remaining
                print("You have", attempts, "attempts remaining")
            print('--------------------------------------------------')




    def mystery_word(self, mystery_word):
        stars = ""
        for x in range(len(mystery_word)):
            stars += "*"
        return stars
