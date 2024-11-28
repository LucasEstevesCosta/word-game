# pylint: disable=consider-using-enumerate

class PlaysManager:
    """Manages the game plays."""
    def __init__(self, game_state, input_handler, results):
        self.game_state = game_state
        self.input_handler = input_handler
        self.current_play = 0
        self.results = results

    def play(self) -> None:
        """
        Plays the game.
        Args:
            None
        Returns:
            None
        """
        """PRINT STATEMENT FOR DEBUGGING ONLY"""
        print(self.game_state.random_word)

        while True:
            guess = self.input_handler.player_play()
            if self.input_handler.has_numbers(guess):
                print('PALAVRA INVÁLIDA. Essa palavra contem números.')
                return
            self.game_state.update_player_guess(guess)
            # Update the game state and check if the player won
            self.check_play()
            # Show the current game result
            self.results.show_result()

            if self.current_play == self.game_state.number_of_chances:
                self.results.game_over()
                break

            if self.game_state.player_win:
                self.results.game_won()
                break

    def check_play(self) -> None:
        """
        Checks if the player has won the game.
        Args:
            None
        Returns:
            None
        """
        if self.game_state.player_guess == list(self.game_state.random_word):
            # Update the player win status
            self.game_state.update_player_win(True)
        else:
            # Update the temporary result and incorrect letters list
            self.update_temp_result()
            # Increment the current play count
            self.results.update_current_play()
            # Update the incorrect letters list
            self.update_incorrect_letters_list()
            # Update the right letter wrong place list
            self.update_right_letter_wrong_place_list()

    def update_temp_result(self) -> None:
        """
        Updates the temporary result with the correctly guessed letters.
        Args:
            None
        Returns:
            None
        """
        temp_result = ['?'] * len(self.game_state.random_word)
        for i, letter in enumerate(self.game_state.player_guess):
            if letter == self.game_state.random_word[i]:
                temp_result[i] = letter
        self.game_state.update_temp_result(temp_result)

    def update_incorrect_letters_list(self) -> None:
        """
        Updates the incorrect letters list with the incorrectly guessed letters.
        Args:
            None
        Returns:
            None
        """
        incorrect_letters_list = []
        for letter in self.game_state.player_guess:
            if letter not in self.game_state.random_word:
                incorrect_letters_list.append(letter)
        self.game_state.update_incorrect_letters_list(incorrect_letters_list)

    def update_right_letter_wrong_place_list(self) -> None:
        """
        Updates the right letter wrong place list with the incorrectly
        guessed letters in the wrong place.
        Args:
            None
        Returns:
            None
        """
        right_letter_wrong_place_list = []
        for i, letter in enumerate(self.game_state.player_guess):
            if letter in self.game_state.random_word and letter != self.game_state.random_word[i]:
                if letter not in self.game_state.right_letter_wrong_place_list:
                    letter_count = self.game_state.random_word.count(letter)
                    self.game_state.right_letter_wrong_place_list.extend([letter] * letter_count)
        self.game_state.update_right_letter_wrong_place_list(right_letter_wrong_place_list)
