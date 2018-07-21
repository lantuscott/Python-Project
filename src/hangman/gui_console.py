# import src.hangman.Word

import turtle as t
from src.hangman import Word

class gui_console:

    def __init__(self):
        console_word = Word()
        console_word.game_logic()

    def game_screen(self):
        wn = t.Screen()
        tess = t.Turtle()
        t.begin_fill()

    # t.done()

nsmr = gui_console()

