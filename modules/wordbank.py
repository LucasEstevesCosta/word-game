# pylint: disable=consider-using-enumerate
from random import choice


class WordBank:
    """
    A class to manage a word bank loaded from a text file.

    Attributes:
        wordslist (list): A list containing all the words loaded from the file.
    """

    def __init__(self, filename='word-bank.txt'):
        """
        Initializes the WordBank object.

        Args:
            filename (str): The name of the file containing the word bank.
                Defaults to 'word-bank.txt'.

        Attributes:
            filename (str): The name of the file containing the word bank.
            wordslist (list): A list of words from the word bank file.
        """
        self.filename = filename
        self.wordslist = self.create_word_bank()
        self.chosen_word = self.choose_random_word()

    def create_word_bank(self) -> list:
        """
        Reads a list of words from a file and returns them as a list.

        This method reads a file named 'word-bank.txt' and creates a list of words
        from it. It handles various exceptions that may occur during the file reading process.

        Args:
            None

        Returns:
            list: A list of words read from the file.

        Raises:
            FileNotFoundError: If the file 'word-bank.txt' is not found.
            IOError: If an error occurs while reading the file.
            ValueError: If the file is empty.
            Exception: For any other unexpected error.
        """
        word_bank = list()
        try:
            with open('word-bank.txt', 'r', encoding='utf-8') as words_file:
                word_bank = [word.strip()
                             for word in words_file if word.strip()]

                if not word_bank:
                    raise ValueError(f'O arquivo {self.filename} está vazio')

        except FileNotFoundError:
            print(f'O arquivo {self.filename} não foi encontrado.')
            raise
        except IOError as error:
            print(f'ERRO: Falha ao ler o arquivo {
                  self.filename}. Erro: {error}')
            raise
        except Exception as error:
            print(f'ERRO. Erro inesperado ao processar o arquivo: {error}')
            raise

        return word_bank

    def choose_random_word(self) -> str:
        """
        Selects a random word from the list of words.

        Args:
            None

        Returns:
            str: A randomly chosen word from the wordslist.
        """
        word = choice(self.wordslist)
        return [letter for letter in word]


class PlaysManager():
    """
    Manages the gameplay logic for the game.

    Attributes:
        player_guess (str): The player's current guess for the word. Initialized as an empty string.
        chosen_word (str): The secret word that the player is trying to guess.
    """

    def __init__(self, chosen_word, player_name):
        """
        Initializes a new PlaysManager instance.

        Args:
            chosen_word (str): The secret word to be guessed.
        """
        self.player_guess = list()
        self.chosen_word = chosen_word
        self.incorrect_letters = list()
        self.right_letter_wrong_place = list()
        self.temp_result = self.temp_result = ['?'] * len(self.chosen_word)
        self.player_win = False
        self.player_name = player_name

    @staticmethod
    def player_play() -> list:
        """
        Prompts the player to guess a 5-letter word and validates the input.

        This method repeatedly asks the player to input a 5-letter word until
        a valid guess is provided.

        Returns:
            str: The player's valid 5-letter guess.
        """
        while True:
            guess = str(
                (input('Digite qual palavra de 5 letras estou pensando: '))).upper().strip()
            if 4 > len(guess) > 6:
                print('Digite apenas palavras de 5 letras.')
                continue
            if PlaysManager.has_numbers(guess):
                print('Palavra inválida. Você digitou uma palavra com números.')
                continue
            return [letter for letter in guess]

    @staticmethod
    def has_numbers(word):
        """Checks if a given word contains any numbers.

        Args:
            word: The word to check.

        Returns:
            True if the word contains at least one number, False otherwise.
        """
        return any(l.isdigit() for l in word)

    def compare_words(self) -> bool:
        """
        Compares the player's guess to the chosen word and updates the game state accordingly.

        This method iterates through each letter in the player's guess and compares it to the corresponding
        letter in the chosen word. It updates the `temp_result`, `incorrect_letters`, and `right_letter_wrong_place`
        attributes based on the comparison. If the player's guess matches the chosen word, it sets the `player_win`
        attribute to True.

        Returns:
            bool: True if the player has won, False otherwise.
        """
        for i in range(len(self.player_guess)):
            letter = self.player_guess[i]

            self.check_letter_not_in_result(letter)

            self.check_letter_wrong_place(letter, self.chosen_word[i])

            self.check_right_word_right_place(letter, self.chosen_word[i], i)

            if str(self.temp_result) == str(self.chosen_word):
                self.player_win = True
                break

    def check_right_word_right_place(self, letter: str, right_letter: str, index: int) -> None:
        """Checks if a letter is in the correct position in the guessed word.

        If the letter is in the correct position, it updates the temporary result
        and removes it from the dictionary of letters that are in the word but
        in the wrong position.

        Args:
            letter (str): The letter from the guessed word.
            right_letter (str): The corresponding letter from the target word.
            index (int): The index of the letter in the guessed word.
        """
        if letter == right_letter:
            self.temp_result[index] = letter
            if letter in self.right_letter_wrong_place:
                self.right_letter_wrong_place.remove(letter)

    def check_letter_not_in_result(self, letter: str) -> None:
        """
        Checks if a given letter is not in the chosen word and has not been guessed incorrectly.

        Args:
            letter (str): The letter to check.

        Returns:
            bool: True if the letter is not in the chosen word and has not been guessed incorrectly, False otherwise.
        """
        if letter not in self.chosen_word:
            if letter not in self.incorrect_letters:
                self.incorrect_letters.append(letter)

    def check_letter_wrong_place(self, letter: str, right_letter: str) -> None:
        """
        Checks if the given letter is in the chosen word but in the wrong place.

        This method updates the `right_letter_wrong_place` list with the given letter if it meets the following conditions:

        1. The letter is present in the chosen word (`self.chosen_word`).
        2. The letter is not the same as the right letter (`right_letter`).
        3. The letter is not already present in the `right_letter_wrong_place` list.

        Args:
            letter (str): The letter to check.
            right_letter (str): The correct letter in the chosen word.

        Returns:
            None
        """
        if letter in self.chosen_word and letter != right_letter:
            if letter not in self.right_letter_wrong_place:
                letter_count = self.chosen_word.count(letter)
                self.right_letter_wrong_place.extend([letter] * letter_count)

    def game_play(self):
        """
        Manages the game flow, allowing the player to guess letters until they win or run out of chances.

        This method controls the main game loop, allowing the player to guess letters, compare their guesses to the chosen word,
        and display the current game status. It also handles winning and losing conditions.

        Attributes:
            number_of_chances (int): The total number of chances the player has to guess the word.
            current_play (int): The current attempt number.
            player_win (bool): Flag indicating whether the player has won the game.

        Raises:
            None

        Returns:
            None

        Side Effects:
            Updates the game state, including the player's guesses, the result, and the number of remaining chances.
            Prints game information and messages.
        """
        number_of_chances = 5
        current_play = 0
        while True:
            self.player_guess = self.player_play()
            self.compare_words()

            if self.player_win:
                if current_play == 0:
                    print('WOW! Você acertou de primeira. QUE CAGADA!')
                    print('Fim de jogo.')
                    quit()
                else:
                    print(f'PARABÉNS {self.player_name}! Você acertou!')
                    print('Fim de jogo.')
                    quit()

            print(f'RESULTADO ATUAL: {self.temp_result}')
            print(f'LETRAS QUE ERROU A POSIÇÃO: {
                  self.right_letter_wrong_place}')
            print(f'LETRAS ERRADAS: {self.incorrect_letters}')

            current_play += 1
            print(f'TENTATIVAS RESTANTES: {number_of_chances - current_play}')
            if current_play == number_of_chances:
                print(f'Que peninha {
                      self.player_name}. Você não conseguiu acertar e suas chances acabaram.')
                print(f'A palavra era {
                      ''.join(self.chosen_word)}. Mais sorte na próxima!')
                print('Fim de jogo.')
                quit()
            print()
            print()
