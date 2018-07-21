# Leonardo Farinha

import threading


def main():
    import src.hangman.Word as Word
    game = Word.Word()
    game.game_logic()


if __name__ == '__main__':
    main()
