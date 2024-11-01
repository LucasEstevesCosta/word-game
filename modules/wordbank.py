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
            print(f'ERRO: Falha ao ler o arquivo {self.filename}. Erro: {error}')
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
        self.temp_result = self.temp_result = ['_'] * len(self.chosen_word)
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

    def compare_words(self):
        placeholder = '_'
        for i in range(len(self.player_guess)):
            if self.player_guess[i] not in self.chosen_word:
                if self.player_guess[i] not in self.incorrect_letters:
                    self.incorrect_letters.append(self.player_guess[i])
            else:
                if self.player_guess[i] == self.chosen_word[i]:
                    self.temp_result[i] = self.player_guess[i]
                else:
                    if not self.temp_result[i]:
                        self.temp_result[i] = placeholder
                        if self.player_guess[i] not in self.right_letter_wrong_place:
                            self.right_letter_wrong_place.append(self.player_guess[i])

            if str(self.temp_result) == str(self.chosen_word):
                self.player_win = True
                break

    def game_play(self):
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
            print(f'LETRAS QUE ERROU A POSIÇÃO: {self.right_letter_wrong_place}')
            print(f'LETRAS ERRADAS: {self.incorrect_letters}')

            current_play += 1
            print(f'TENTATIVAS RESTANTES: {number_of_chances - current_play}')
            if current_play == number_of_chances:
                print(f'Que peninha {self.player_name}. Você não conseguiu acertar e suas chances acabaram.')
                print(f'A palavra era {''.join(self.chosen_word)}. Mais sorte na próxima!')
                print('Fim de jogo.')
                quit()
            print()
            print()
