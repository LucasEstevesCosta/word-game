from classes.WordBank import WordBank

GAME_NAME = 'Quasi-Forca'


def main() -> None:
    print(f"Bem-vindo ao {GAME_NAME}!")

    # Crie uma instância da classe WordBank
    word_bank = WordBank()
    chosen_word = word_bank.choose_random_word()

    print(chosen_word)


if __name__ == '__main__':
    main()
