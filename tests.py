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
            
            """ # if the letter is not on the word
            if self.player_guess[i] not in self.chosen_word:
                # if the letter is not on the incorrect letter list
                if self.player_guess[i] not in self.incorrect_letters:
                    # place the letter on the incorrect letter list
                    self.incorrect_letters.append(self.player_guess[i])

            else:  # if the letters are equals AND...
                # in the same position
                if self.player_guess[i] == self.chosen_word[i]:
                    self.temp_result[i] = self.player_guess[i]
                    if self.player_guess[i] in self.right_letter_wrong_place:
                        self.right_letter_wrong_place.remove(self.player_guess[i])

                else:  # not on the same position
                    # if the letter is not on the correct word but wrong place list
                    if self.player_guess[i] not in self.right_letter_wrong_place:
                        # puts on the list if the letter repeats itself
                        for i in range(self.chosen_word.count(self.player_guess[i])):
                            self.right_letter_wrong_place.append(self.player_guess[i])
                        if self.temp_result[i] == '?':  # if the place is empty
                            self.temp_result[i] = placeholder"""