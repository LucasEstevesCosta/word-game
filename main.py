from random import randint
from classes.WordBank import WordBank

GAME_NAME = 'Quasi-Forca'


def main() -> None:
    print(f"Bem-vindo ao {GAME_NAME}!")

    # Crie uma instância da classe WordBank
    word_bank = WordBank()
    print(word_bank.wordslist)


if __name__ == '__main__':
    main()
