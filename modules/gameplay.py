# pylint: disable=consider-using-enumerate
class PlaysManager():
    def __init__(self, random_word, player_name):
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
        """
        Checks if a given word contains any numbers.
        This method uses the any() function to check if any of the characters in the word are digits.
        Args:
            word (str): The word to be checked.
        Returns:
            bool: True if the word contains any numbers, False otherwise.
        """
        return any(l.isdigit() for l in word)

    def game_play(self):
        """
        Starts the game loop.
        Args:
            None
        Returns:
            None
        """
        number_of_chances = 5
        current_play = 0
        print(self.random_word)
        while True:
            self.player_guess = self.player_play()
            self.compare_words()
            self.check_player_won(current_play)
            self.show_result(number_of_chances, current_play)
            current_play += 1
            self.check_game_over(number_of_chances, current_play)

    def compare_words(self) -> bool:
        """
        Compares the player's guessed word with the random word.
        This method iterates over each letter in the player's guess and performs the following checks:
            - If a letter is not in the random word, it is added to the list of incorrect letters.
            - If a letter is in the wrong place, it is recorded in the right_letter_wrong_place_list list.
            - If a letter is in the correct place, it updates the temp_result to reflect the correct guess.
        If the player's guess matches the random word, the player is marked as having won the game.
        Args:
            None
        Returns:
            bool: True if the player's guess matches the random word, False otherwise.
        """
        for i in range(len(self.player_guess)):
            letter = self.player_guess[i]

            self.check_letter_not_in_result(letter)
            self.check_letter_wrong_place(letter, self.random_word[i])
            self.check_right_word_right_place(letter, self.random_word[i], i)

            if str(self.player_guess) == str(self.random_word):
                self.player_win = True
                break

    def check_letter_not_in_result(self, letter: str) -> None:
        """
        Checks if the letter is not in the random word.
        If the letter is not in the random word, it is added to the list of incorrect letters.
        Args:
            letter (str): The letter to be checked.
        """
        if letter not in self.incorrect_letters_list:
            self.incorrect_letters_list.append(letter)

    def check_letter_wrong_place(self, letter: str, right_letter: str) -> None:
        """
        Checks if the letter is in the wrong place.
        If the letter is in the wrong place, counts how many times the letter appears in the random word and
        adds it to the right_letter_wrong_place_list only if it is not already there.
        Args:
            letter (str): The letter to be checked.
            right_letter (str): The correct letter in the same position.
        """
        if letter in self.random_word and letter != right_letter:
            if letter not in self.right_letter_wrong_place_list:
                letter_count = self.random_word.count(letter)
                self.right_letter_wrong_place_list.extend(
                    [letter] * letter_count)

    def check_right_word_right_place(self, letter: str, right_letter: str, index: int) -> None:
        """
        Checks if the letter is in the right place.
        If the letter is in the right place, it is recorded in temp_result.
        Count the number of occurrences of the letter
        if the letter is not in right_letter_wrong_place_list add it to the list the number of times it appears
        if the letter is right_letter_wrong_place_list remove it from the list one time.
        Args:
            letter (str): The letter to be checked.
            right_letter (str): The correct letter in the same position.
            index (int): The index of the letter in the random word.
        """
        if letter == right_letter:
            self.temp_result[index] = letter
            if letter not in self.right_letter_wrong_place_list:
                letter_count = self.random_word.count(letter)
                self.right_letter_wrong_place_list.extend(
                    [letter] * letter_count)
            if letter in self.right_letter_wrong_place_list:
                self.right_letter_wrong_place_list.remove(letter)

    def check_player_won(self, current_play: int) -> None:
        """
        Checks if the player has won the game.
        If the player has won, the game ends with a message of congratulations.
        Args:
            current_play (int): The number of the current play.
        """
        if self.player_win:
            if current_play == 0:
                print('WOW! Você acertou de primeira. QUE CAGADA!')
                print('Fim de jogo.')
                quit()
            else:
                print(f'PARABÉNS {self.player_name}! Você acertou!')
                print('Fim de jogo.')
                quit()

    def show_result(self, number_of_chances: int, current_play: int) -> None:
        """
        Displays the current game result, including correctly guessed letters,
        letters guessed in the wrong position, incorrect letters, and remaining attempts.
        This function provides feedback to the player by printing the current state of their guesses 
        and any mistakes. It keeps the player informed about their progress and remaining opportunities 
        to guess the correct word.
        Args:
            number_of_chances (int): The total number of chances the player has to guess the word.
            current_play (int): The current play count, representing how many attempts have been made.
        Returns:
            None
        """
        print(f'RESULTADO ATUAL: {self.temp_result}')
        print(f'LETRAS QUE ERROU A POSIÇÃO: {self.right_letter_wrong_place_list}')
        print(f'LETRAS ERRADAS: {self.incorrect_letters_list}')
        print(f'TENTATIVAS RESTANTES: {number_of_chances - current_play}')

    def check_game_over(self, number_of_chances: int, current_play: int) -> None:
        """
        Checks if the game is over due to the player's number of chances.
        If the game is over, the game ends with a message of condolences.
        Args:
            number_of_chances (int): The total number of chances the player has to guess the word.
            current_play (int): The current play count, representing how many attempts have been made.
        Returns:
            None
        """
        if current_play == number_of_chances:
            print(f'Que peninha {self.player_name}. Você não conseguiu acertar e suas chances acabaram.')
            print(f'A palavra era {''.join(self.random_word)}. Mais sorte na próxima!')
            print('Fim de jogo.')
            quit()
        print()
        print()
