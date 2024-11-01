from modules.wordbank import WordBank, PlaysManager
from time import sleep

GAME_NAME = 'Quasi-Forca'


def main() -> None:
    print(f"Bem-vindo ao {GAME_NAME}!")
    print('Nesse jogo você precisa descobrir qual é a palavra de 5 letras. Você tem 5 chances.')
    sleep(2)

    # Asks if the user want to play
    start_game = input('Deseja jogar [SIM] ou [NÃO]? ')
    if start_game.lower() != 'sim':
        print('Ah, que pena. Espero te ver novamente!')
        quit()

    # Asks the player name
    player_name = input('Me diga qual é o seu nome: ').title()
    print()
    print()

    word_bank = WordBank()
    manager = PlaysManager(word_bank.chosen_word, player_name)
    manager.game_play()


if __name__ == '__main__':
    main()
