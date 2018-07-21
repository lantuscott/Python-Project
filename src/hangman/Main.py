# Leonardo Farinha

import threading


def main():
    import src.hangman.Word as Word
    import src.hangman.Drawer as Drawer
    import src.hangman.Beast as Beast

    # game = Beast.Beast()


    game = Word.Word()
    game.game_logic()

    # gui = Drawer.Drawer()







if __name__ == '__main__':
    main()
