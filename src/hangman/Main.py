# Leonardo Farinha


def main():
    import src.hangman.Word as Word
    import src.hangman.GuiConsole as Gui
    gameStart = Word.Word()
    gameStart.game_logic()
    guivaina = Gui.GuiConsole()
    guivaina.game_screen()


if __name__ == '__main__':
    main()
