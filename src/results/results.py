class Results:
    """
    Manages the game results and provides feedback to the player.
    Attributes:
        game_state (GameState): The current game state.
        current_play (int): The current play count, representing how many
        attempts have been made.
    """
    def __init__(self, game_state):
        self.game_state = game_state
        self.current_play = 0

    def update_current_play(self) -> None:
        """
        Updates the current play count.
        Args:
            current_play (int): The current play count, representing how many
            attempts have been made.
        Returns:
            None
        """
        self.current_play = self.current_play + 1

    def show_result(self) -> None:
        """
        Displays the current game result, including correctly guessed letters,
        letters guessed in the wrong position, incorrect letters, and remaining attempts.
        This function provides feedback to the player by printing the current state of their guesses 
        and any mistakes. It keeps the player informed about their progress and remaining
        opportunities 
        to guess the correct word.
        Args:
            number_of_chances (int): The total number of chances the player has to guess the word.
            current_play (int): The current play count, representing how
            many attempts have been made.
        Returns:
            None
        """
        print(f'RESULTADO ATUAL: {self.game_state.temp_result}')
        print(f'LETRAS QUE ERROU A POSIÇÃO: {self.game_state.right_letter_wrong_place_list}')
        print(f'LETRAS ERRADAS: {self.game_state.incorrect_letters_list}')
        print(f'TENTATIVAS RESTANTES: {self.game_state.number_of_chances - self.current_play}')

    def game_over(self) -> None:
        """
        Displays a message indicating that the game has ended.
        Args:
            None
        Returns:
            None
        """
        print(f'Que peninha {self.game_state.player_name}.', end=' ')
        print('Você não conseguiu acertar e suas chances acabaram.')
        print(f'A palavra era {''.join(self.game_state.random_word)}. Mais sorte na próxima!')
        print('Fim de jogo.')
        print()
        print()

    def game_won(self) -> None:
        """
        Displays a message indicating that the player has won the game.
        Args:
            current_play (int): The current play count, representing how many
            attempts have been made.
        Returns:
            None
        """
        if self.game_state.player_win:
            if self.game_state.current_play == 0:
                print('WOW! Você acertou de primeira. QUE CAGADA!')
                print('Fim de jogo.')
                quit()
            else:
                print(f'PARABÉNS {self.game_state.player_name}! Você acertou!')
                print('Fim de jogo.')
                quit()
