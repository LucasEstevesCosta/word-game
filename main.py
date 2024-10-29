from classes.WordBank import WordBank, PlaysManager

GAME_NAME = 'Quasi-Forca'
NUMBER_OF_CHANCES = 5


def main() -> None:
    print(f"Bem-vindo ao {GAME_NAME}!")
    print('Nesse jogo você precisa descobrir qual é a palavra de 5 letras. Você tem 5 chances.')
    
    # Asks if the user want to play
    start_game = input('Deseja jogar [SIM] ou [NÃO]? ')
    if start_game.lower() != 'sim':
        print('Ah, que pena. Espero te ver novamente!')
        quit()

    # Asks the player name
    player_name = input('Me diga qual é o seu nome: ')
    
    # Creates an instance of the class WordBank
    word_bank = WordBank()
    chosen_word = word_bank.choose_random_word()
    manager = PlaysManager(chosen_word)
    manager.player_guess()

    right_letter_wrong_place = []
    incorrect_letters = []
    current_number_of_chances = NUMBER_OF_CHANCES


if __name__ == '__main__':
    main()
