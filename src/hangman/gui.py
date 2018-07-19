#
#  This script contains the GUI management for the game.
#
from tkinter import Tk, Label, Button, Frame, Entry, StringVar, Canvas
import turtle

from src.hangman.Word import Word


class Hangman:
    """
    This class creates a list of words and does different things to it like returning the list
    """

    def __init__(self):
        self.dictionary = Word()

        self.root = Tk()
        self.root.title("Hangman, The NEWER")

        self.canvas = Canvas(master=self.root, width=800, height=600)
        self.canvas.pack()

        leo = turtle.RawTurtle(self.canvas)
        leo.shape("turtle")
        # leo.forward(100)

        letter = StringVar()
        self.word = Entry(self.root, textvariable=letter, width=2)
        self.word.pack()

        self.label = Label(self.root, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = Button(self.root, text="Greet", command=lambda: self.move_turtle(leo))
        self.greet_button.pack()

        self.root.mainloop()

    @staticmethod
    def move_turtle(leo):
        return leo.forward(100)


def main():
    # creates and object and starts the game
    game = Hangman()


if __name__ == '__main__':
    main()
