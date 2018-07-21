# import src.hangman.Word

import turtle as t

class GuiConsole:

    def game_screen(self):
        wn = t.Screen()
        tess = t.Turtle()
        t.begin_fill()
        t.exitonclick()


def main():
    import src.hangman.Word as Word
    gameStart = Word.Word()
    gameStart.game_logic()
    guivaina = GuiConsole()
    guivaina.game_screen()


if __name__ == '__main__':
    main()
