class GameState:
    """
    A class to represent the game state.

    Attributes:
        player_guess (list): A list to store the player's current guess.
        random_word (str): The word to be guessed by the player.
        incorrect_letters_list (list): A list of letters that the player guessed incorrectly.
        right_letter_wrong_place_list (list): A list of letters guessed correctly but in the wrong place.
        temp_result (list): A temporary result to track the player's progress in guessing the word.
        player_win (bool): A flag indicating whether the player has won the game.
        player_name (str): The name of the player.
    """
    def __init__(self, random_word, player_name, number_of_chances):
        """
        Initializes the PlaysManager object with a random word and player name.

        This constructor sets up the game state, including the player's guesses, 
        the random word to be guessed, and various lists to track incorrect letters 
        and letters guessed in the wrong place. It also initializes the player's win 
        status and stores the player's name.
        Args:
            random_word (str): The word that the player needs to guess.
            player_name (str): The name of the player.
        Attributes:
            player_guess (list): A list to store the player's current guess.
            random_word (str): The word to be guessed by the player.
            incorrect_letters_list (list): A list of letters that the player guessed incorrectly.
            right_letter_wrong_place_list (list): A list of letters guessed correctly but in the wrong place.
            temp_result (list): A temporary result to track the player's progress in guessing the word.
            player_win (bool): A flag indicating whether the player has won the game.
            player_name (str): The name of the player.
        """
        self.player_guess = list()
        self.random_word = random_word
        self.incorrect_letters_list = list()
        self.right_letter_wrong_place_list = list()
        self.temp_result = self.temp_result = ['?'] * len(self.random_word)
        self.player_win = False
        self.player_name = player_name
        self.number_of_chances = number_of_chances

    def update_player_guess(self, guess):
        """Updates the player's guess."""
        self.player_guess = guess

    def update_temp_result(self, temp_result):
        """Updates the temporary result."""
        self.temp_result = temp_result

    def update_incorrect_letters_list(self, incorrect_letters_list):
        """Updates the incorrect letters list."""
        self.incorrect_letters_list = incorrect_letters_list

    def update_right_letter_wrong_place_list(self, right_letter_wrong_place_list):
        """Updates the right letter wrong place list."""
        self.right_letter_wrong_place_list = right_letter_wrong_place_list

    def update_player_win(self, player_win):
        """Updates the player's win status."""
        self.player_win = player_win
