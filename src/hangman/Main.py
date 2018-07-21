# Leonardo Farinha


def main():
    import src.hangman.Word as Word
    import src.hangman.Drawer as Drawer
    gameStart = Word.Word()
    gameStart.game_logic()
    guivaina = Drawer.GuiConsole()
    guivaina.game_screen()


if __name__ == '__main__':
    main()
