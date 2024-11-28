from src.wordBank.word_bank import WordBank
from src.gameState.game_state import GameState
from src.gamePlay.game_play import PlaysManager
from src.inputHandler.input_handler import InputHandler
from src.results.results import Results

GAME_NAME = 'Quasi-Forca'
NUMBER_OF_CHANCES = 5


def main() -> None:
    """
    The main function that starts the game.
    """
    print(f"Bem-vindo ao {GAME_NAME}!")
    print('Nesse jogo você precisa descobrir qual é a palavra de 5 letras. Você tem 5 chances.')

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
    game_state = GameState(random_word, player_name, NUMBER_OF_CHANCES)
    input_handler = InputHandler()
    results = Results(game_state)
    plays_manager = PlaysManager(game_state, input_handler, results)

    plays_manager.play()


if __name__ == '__main__':
    main()
