import random

class Hangman:
    # List of 10 pre defined word
    words = ["python", "programmering", "dator", "algoritm", "utveckling", "kodning", "debugger", "variabel", "funktion", "loop"]

    def __init__(self):
        self.word = random.choice(self.words)
        self.word_letters = set(self.word)
        self.guessed_letters = set()
        self.attempts = 20
        self.message = "Welocme to Hangman! Please guess a letter."

    def guess(self, letter):
        if self.is_game_over():
            return

        if letter in self.guessed_letters:
            self.message = "You have already guessed this letter. Please try again!"
        elif letter in self.word_letters:
            self.word_letters.remove(letter)
            self.guessed_letters.add(letter)
            self.message = "Correct!"
        else:
            self.attempts -= 1
            self.guessed_letters.add(letter)
            self.message = "Sorry, this letter does not exist in the word."

        if self.is_game_over():
            if self.attempts == 0:
                self.message = f"Sorry, Game over :( The word is {self.word}."
            else:
                self.message = f"Congratulations! You guessed the word: {self.word}"

    def display_word(self):
        return ''.join(letter if letter in self.guessed_letters else '_' for letter in self.word)

    def is_game_over(self):
        return self.attempts == 0 or len(self.word_letters) == 0

    def to_dict(self):
        return {
            'word': self.word,
            'word_letters': list(self.word_letters),
            'guessed_letters': list(self.guessed_letters),
            'attempts': self.attempts,
            'message': self.message
        }

    @classmethod
    def from_dict(cls, data):
        game = cls()
        game.word = data['word']
        game.word_letters = set(data['word_letters'])
        game.guessed_letters = set(data['guessed_letters'])
        game.attempts = data['attempts']
        game.message = data['message']
        return game