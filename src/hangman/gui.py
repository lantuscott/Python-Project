#
#  This script contains the GUI management for the game.
#
from tkinter import Tk, Label, Button, Entry, StringVar, Canvas, LEFT
import turtle
from src.hangman.Word import Word


class Hangman:
    """
    This class creates a list of words and does different things to it like returning the list
    """

    def __init__(self):
        Word.read_words_from_file()
        self.my_word = Word.random_word()

        self.root = Tk()
        self.root.title("Hangman, The NEWER")

        self.canvas = Canvas(master=self.root, width=800, height=600)
        self.canvas.pack()

        leo = turtle.RawTurtle(self.canvas)
        leo.shape("turtle")
        # leo.forward(100)

        letter = StringVar()
        self.word = Entry(self.root,
                          textvariable=letter,
                          width=2)
        self.word.pack()

        self.answer = Button(self.root,
                             text="Peek!",
                             command=lambda: self.validate_letter(self.my_word, self.word.get(), leo))
        self.answer.pack()

        # self.word_label = Label(self.canvas, text="_", font=("Helvetica", 30))
        # self.word_label.pack(side=LEFT)

        self.generate_labels(self.root,
                             self.my_word)

        self.root.mainloop()

    @staticmethod
    def move_turtle(leo):
        return leo.circle(60)

    @staticmethod
    def validate_letter(dictionary, word, leo):
        print("Called method.")
        if word in dictionary:
            print("Letter is there!", dictionary)
            Hangman.show_letters(word, )
        else:
            print("Wrong!", dictionary)
            Hangman.move_turtle(leo)

    @staticmethod
    def show_letters(letter, label):
        label.set(letter)

    @staticmethod
    def generate_labels(root, word):
        labels = []
        for x in range(len(word)):
            labels.append(Label(root, text="_", font=("Helvetica", 30)))
            labels[x].place(x=500 + (50 * x), y=700)
            print(labels[x])


def main():
    # creates and object and starts the game
    game = Hangman()


if __name__ == '__main__':
    main()
