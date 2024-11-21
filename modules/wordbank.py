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
        self.random_word = self.choose_random_word()

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
