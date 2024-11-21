from modules.wordbank import WordBank
from modules.gameplay import PlaysManager
from time import sleep

GAME_NAME = 'Quasi-Forca'


def main() -> None:
    print(f"Bem-vindo ao {GAME_NAME}!")
    print('Nesse jogo você precisa descobrir qual é a palavra de 5 letras. Você tem 5 chances.')
    sleep(2)

    # Asks if the user want to play
    start_game = input('Deseja jogar [SIM] ou [NÃO]? ')
    if start_game.lower() == 'não' or start_game == 'nao':
        print('Ah, que pena. Espero te ver novamente!')
        quit()

    # Asks the player name
    player_name = input('Me diga qual é o seu nome: ').title()
    print()
    print()

    word_bank = WordBank()
    random_word = word_bank.random_word
    manager = PlaysManager(random_word, player_name)
    manager.game_play()


if __name__ == '__main__':
    main()
