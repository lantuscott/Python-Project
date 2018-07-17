#
#  This script contains the GUI management for the game.
#
from tkinter import Tk, Label, Button, Frame, Entry, StringVar


class Hangman:

    """
    This class creates a list of words and does different things to it like returning the list
    """

    def __init__(self, canvas):
        self.canvas = canvas
        canvas.title("Hangman, The NEWER")

        self.frame = Frame(canvas, width=800, height=600)
        self.frame.pack()

        letter = StringVar()
        self.word = Entry(canvas, textvariable=letter, width=2)
        self.word.pack()

        self.label = Label(canvas, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = Button(canvas, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(canvas, text="Close", command=canvas.quit)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")


root = Tk()
canvas = Hangman(root)
root.mainloop()


