from modules.wordbank import WordBank, PlaysManager

wordbank = WordBank()
manager = PlaysManager(wordbank.chosen_word)

test1 = manager.player_play()
print(test1)

def compare_words(self):
        placeholder = '_'
        self.temp_result = [''] * len(self.player_guess)
        for i in range(len(self.player_guess)):
            if self.player_guess[i] not in self.chosen_word:
                self.incorrect_letters.append(self.player_guess[i])

            elif self.player_guess[i] == self.chosen_word[i]:
                if self.temp_result[i] == placeholder or not self.temp_result[i]:
                    self.temp_result[i] = self.player_guess[i]
                else:
                    self.right_letter_wrong_place.append(self.player_guess[i])
                    self.temp_result[i] = placeholder

            if str(self.temp_result) == str(self.chosen_word):
                self.player_win = True
                break