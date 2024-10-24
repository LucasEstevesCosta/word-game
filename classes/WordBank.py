from random import randint

class WordBank:
    """
       Classe para gerenciar um banco de palavras carregado de um arquivo texto.

       Attributes:
           wordslist (list): Lista contendo todas as palavras carregadas do arquivo.
       """
    def __init__(self, filename='word-bank.txt'):
        """
       Inicializa o WordBank carregando palavras do arquivo especificado.

       Args:
           filename (str): Nome do arquivo contendo o banco de palavras. O padrão é 'word-bank.txt'.
       """
        self.filename = filename
        self.wordslist = self.create_word_bank()

    def create_word_bank(self) -> list:
        """
        Cria o banco de palavras lendo de um arquivo texto.

        Returns:
            list: Lista de palavras carregadas do arquivo.

        Raises:
            FileNotFoundError: Se o arquivo não for encontrado.
            IOError: Se houver erro na leitura do arquivo.
        """
        word_bank = list()
        try:
            with open('word-bank.txt', 'r', encoding='utf-8') as words_file:
                word_bank = [word.strip() for word in words_file if word.strip()]

                if not word_bank:
                    raise ValueError(f'O arquivo {self.filename} está vazio')

        except FileNotFoundError:
            print(f'O aquivo {self.filename} não foi encontrado.')
            raise
        except IOError as error:
            print(f'ERRO: Falha ao ler o aquivo {self.filename}. Erro: {error}')
            raise
        except Exception as error:
            print(f'ERRO. Erro inesperado ao processar o arquivo: {error}')
            raise

        return word_bank

    def choose_random_word(self) -> str:
        return self.wordslist[randint(0, len(self.wordslist)) - 1]
