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
    attempt_number = 0

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
        path_to_utils = self.path_to_project + "/utils"
        while True:
            letter = input("What difficulty do you want? Easy=e, Medium=m, Hard=h: ")
            if letter in "emh":
                if letter == "e":
                    words = open(path_to_utils + '/easy_words.txt', 'r')
                    self.my_words = words.read().split()
                    words.close()
                    break
                elif letter == "m":
                    words = open(path_to_utils + '/medium_words.txt', 'r')
                    self.my_words = words.read().split()
                    words.close()
                    break
                elif letter == "h":
                    words = open(path_to_utils + '/hard_words.txt', 'r')
                    self.my_words = words.read().split()
                    words.close()
                    break
            elif letter not in "emh":
                print("Input is not valid, Please enter either e for Easy, h for Hard, or m for Hard: ")



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
        list = self.get_my_words()
        word = list[random.randint(0, len(list) - 1)]
        if len(word) > 7:
            while len(word) > 7:
                word = list[random.randint(0, len(list) - 1)]
                if len(word) <= 7:
                    return word
        else:
            return word


    # Checks if letter is in mystery word and tracks number of guesses made and remaining
    def game_logic(self):
        from src.hangman import Drawer
        gui = Drawer.Drawer()
        gui.game_screen()
        original_word_to_guess = self.random_word()
        mystery_word = self.mystery_word(original_word_to_guess)
        acc = 1
        guessed_letters = ''
        progress = ''
        temp = ""
        objectList = [gui]
        methodList = ['draw_base2()']
        remaining_letters = original_word_to_guess
        word_to_list = list(mystery_word)
        print("The word is :", original_word_to_guess)
        print("The word is :", mystery_word)
        print('----------------------------------------------------')
        # User input to guess letter
        program_on = True
        while program_on:
            if temp == '':  # if 0 letters have been guessed it will display mystery word, otherwise it will display your progress
                print("The word is :", mystery_word)
            else:
                print("The word is :", temp)
            print("Attempt #:", acc)
            guess = input("Enter a letter: ")
            guess = guess.lower()  # converts input to lowercase

            # Displays how many guesses you have made
            for attempts in range(1):
                attempts = 10
                attempts = attempts - acc
                word_to_display = original_word_to_guess;

                # Checks if input is valid (a single letter or if the input is same as length of the mystery word)
                if guess in "abcdefghijklmnopqrstuvwxyz":
                    if len(guess) == 1:
                        progress += guess
                        if guess in remaining_letters:
                            remaining_letters = remaining_letters.replace(guess, '')
                            guessed_position = word_to_display.index(guess)
                            word_to_list[guessed_position] = guess
                            temp = "".join(word_to_list)
                            # print("Word is: ", temp)
                            print("you guessed one letter!, remaining letters to be guessed: ", remaining_letters)
                        else:  # Here call the Turtle and create a figure every time a user misses
                            gui.method_factory(self.attempt_number)
                            self.attempt_number += 1
                            print("try again")
                # If input is not valid prints error
                elif guess not in "abcdefghijklmnopqrstuvwxyz":
                    print("Input is not valid, Please enter a letter between 'a' and 'z': ")

                guessed_letters += ' ' + guess
                print("Letters you have tried: ", guessed_letters)

                # When you guess the word, it will compare it with your progress, if it's a match the user wins
                if remaining_letters == "" and attempts > 0:
                    print("You guessed the word! HOORAY!!!", self.attempt_number)
                    gui.you_won()
                    program_on = False
                elif attempts == 0:  # if attempts reach out the max, the user loses
                    print("Game Over!")
                    gui.draw_leftleg()
                    gui.game_over()
                    program_on = False  # I use this to exit the While loop
                # Prints number of guesses remaining
                print("You have", attempts, "attempts remaining")
                acc += 1
            print('--------------------------------------------------')

    def mystery_word(self, mystery_word):
        stars = ""
        for x in range(len(mystery_word)):
            stars += "*"
        return stars


