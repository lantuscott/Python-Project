# Leonardo Farinha
import random
import os
import turtle as t


class Beast:
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
        wn = t.Screen()
        self.game_intro()
        self.game_logic()


    """
    This definition simply put, reads the file containing the words, puts them in a list called my_words
    """

    def read_words_from_file(self):
        path_to_utils = self.path_to_project + "/utils"
        words = open(path_to_utils + '/easy_words.txt', 'r')
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
        original_word_to_guess = self.random_word()
        mystery_word = self.mystery_word(original_word_to_guess)
        acc = 0
        guessed_letters = ''
        progress = ''
        word_to_list = []
        temp = ""
        remaining_letters = original_word_to_guess
        word_to_list = list(mystery_word)
        print("The words is :", original_word_to_guess)
        # User input to guess letter
        while True:
            print("Starred word: ", temp)
            guess = input("Enter a letter: ")
            guess = guess.lower()  # converts input to uppercase

            # Displays how many guesses you have made
            for attempts in range(1):
                attempts = len(original_word_to_guess) * 2
                acc += 1
                print("Attempt #:", acc)
                attempts = attempts - acc
                word_to_display = original_word_to_guess;

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
                            print("try again")
                # If input is not valid prints error
                elif guess not in "abcdefghijklmnopqrstuvwxyz":
                    print("Input is not valid, Please enter a letter between 'a' and 'z': ")
                # Prints number of guesses remaining
                print("You have", attempts, "attempts remaining")

                guessed_letters += ' ' + guess
                print("Letters you have tried: ", guessed_letters)

                # When you guess the word, it will compare it with your progress, if it's a match the user wins
                if remaining_letters == "" and attempts > 0:
                    print("You guessed the word! HOORAY!!!")
                    return 1
                elif attempts <= 0:  # if attempts reach out the max, the user loses
                    print("Game Over!")
                    return -1  # I use this to exit the While loop

    def mystery_word(self, mystery_word):
        stars = ""
        for x in range(len(mystery_word)):
            stars += "*"
        return stars

    def game_screen(self):
        wn = t.Screen()
        # t.speed(1)

        self.game_intro()
        # self.draw_base1()
        # self.draw_base2()
        # self.draw_base3()
        # self.draw_base4()
        # self.draw_circle()
        # self.draw_body()
        # self.draw_rightarm()
        # self.draw_leftarm()
        # self.draw_rightleg()
        # self.draw_leftleg()
        t.exitonclick()

    def game_intro(self):
        t.penup()
        t.goto(-200, 300)
        t.write("Let's play some Hangman!", font=("Calibri", 24, "bold"))

    def draw_base1(self):
        t.goto(-250, -350)
        t.pendown()
        t.begin_fill()
        t.forward(450)
        t.right(90)
        t.forward(50)
        t.right(90)
        t.forward(450)
        t.right(90)
        t.forward(50)
        t.right(90)
        t.end_fill()
        t.penup()
        t.exitonclick()

    def draw_base2(self):
        t.pendown()
        t.begin_fill()
        t.left(90)
        t.forward(550)
        t.right(90)
        t.forward(5)
        t.right(90)
        t.forward(550)
        t.end_fill()
        t.penup()
        t.goto(-250, 200)
        t.left(90)

    def draw_base3(self):
        t.pendown()
        t.forward(230)
        t.penup()

    def draw_base4(self):
        t.pendown()
        t.right(90)
        t.forward(100)
        t.penup()
        t.left(90)

    def draw_circle(self):
        t.goto(-20, 0)
        t.pendown()
        t.circle(50)
        t.penup()

    def draw_body(self):
        t.pendown()
        t.right(90)
        t.forward(200)
        t.penup()

    def draw_rightarm(self):
        t.backward(200)
        t.pendown()
        t.left(55)
        t.forward(150)
        t.penup()

    def draw_leftarm(self):
        t.backward(150)
        t.pendown()
        t.right(110)
        t.forward(150)
        t.penup()

    def draw_rightleg(self):
        t.backward(150)
        t.left(55)
        t.forward(200)
        t.pendown()
        t.left(45)
        t.forward(150)
        t.penup()

    def draw_leftleg(self):
        t.backward(150)
        t.right(90)
        t.pendown()
        t.forward(150)
        t.penup()
