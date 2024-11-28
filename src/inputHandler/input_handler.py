class InputHandler():
    """
    Handles user input for the game.
    """

    @staticmethod
    def player_play() -> list:
        """
        Returns a list of 5 letters entered by the player, after cleaning and validating the input.
        Args:
            None
        Returns:
            list: A list of 5 letters entered by the player.
        """
        while True:
            guess = str(input('Digite qual palavra de 5 letras estou pensando: ')).upper().strip()
            if 4 > len(guess) > 6:
                print('Digite apenas palavras de 5 letras.')
                continue
            return [letter for letter in guess]

    @staticmethod
    def has_numbers(word):
        """
        Checks if a given word contains any numbers.
        This method uses the any() function to check if any of the
        characters in the word are digits.
        Args:
            word (str): The word to be checked.
        Returns:
            bool: True if the word contains any numbers, False otherwise.
        """
        return any(l.isdigit() for l in word)