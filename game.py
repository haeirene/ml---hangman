class Game():
    def __init__(self, mistakes, word_to_be_guessed, word_player_guessed, chosen_word):
        self.mistakes = mistakes
        self.word_to_be_guessed = word_to_be_guessed
        self.word_player_guessed = word_player_guessed
        self.chosen_word = chosen_word
        
        self.start_game()
    
    def start_game(self):
        if(self.word_to_be_guessed == self.word_player_guessed):
            # First we reset everything
            self.word_to_be_guessed = []
            self.word_player_guessed = []

            self.convert_chosen_word_to_be_guessed(self.chosen_word)
            
    # Count how many letters need to be guessed
    def count_letters(self):
        total = 0

        # i = char in word
        for i in self.word_to_be_guessed:
            if(i != " "):
                total += 1

        return total
            
    # Convert the each letter to an unrecognizable word that the player can guess
    def convert_chosen_word_to_be_guessed(self, chosen_word):
        for i in self.chosen_word:
            if(i == " "):
                self.word_to_be_guessed.append(' ')
                self.word_player_guessed.append(' ')
            else:
                self.word_to_be_guessed.append(i)
                self.word_player_guessed.append('_')
    
    def guess(self, guessed_letter):
        # access the global name variable
        is_guessed = self.try_revealing_letters_in_guessed_word(guessed_letter)

        if(is_guessed == False):
            self.mistakes += 1
            
    def make_a_guess(self, guessed_letter):
        has_letter_been_found = False

        for i in self.chosen_word:
            # No space and the letter is in the word
            if(i != " "):
                if(i == guessed_letter):
                    has_letter_been_found = True

                    # Break statement stops the loop
                    break

        return has_letter_been_found
            
    def try_revealing_letters_in_guessed_word(self, guessed_letter):
        is_guessed = self.make_a_guess(guessed_letter)

        # We reveal the letters when the guess was succesfull
        if(is_guessed):
            for idx, i in enumerate(self.word_to_be_guessed):
                if(i == guessed_letter):
                    self.word_player_guessed[idx] = guessed_letter

        return guessed_letter