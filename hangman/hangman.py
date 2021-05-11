import os
import random
from hangman.pics import HANGMAN_PICS


MAX_ATTEMPTS = 7


def clear():
    return os.system('cls')


class Hangman:

    def __init__(self):
        self.remaining_attempts = MAX_ATTEMPTS
        self.failed_attempts = 0
        self.user_chars = []

        self.load_words()

    def load_words(self):
        with open('data/words.txt', 'r', encoding='utf-8') as f:
            words = [line.replace('\n', '') for line in f]

        self.words = words

    def clean_word(self):
        replacements = (
            ('á', 'a'),
            ('é', 'e'),
            ('í', 'i'),
            ('ó', 'o'),
            ('ú', 'u'),
        )

        for a, b in replacements:
            cleaned_word = self.word.replace(a, b)

        self.cleaned_word = cleaned_word

    def select_word(self):
        self.word = random.choice(self.words)
        self.clean_word()

    def print_lines_chars_word(self):
        for char in self.cleaned_word:
            if self.user_chars and char in self.user_chars:
                print(f' {char} ', end='')
            else:
                print(' _ ', end='')
        print()

    def print_game_header(self):
        clear()
        print(' H A N G M A N '.center(50, '*'))
        print()
        print('¡Guess the word!'.ljust(25), end='')
        print(f'Failed attempts: {self.failed_attempts}/{MAX_ATTEMPTS}'
              .rjust(25))
        print()
        self.print_lines_chars_word()

    def print_hangman_pic(self):
        print(HANGMAN_PICS[self.failed_attempts])
        print()

    def refresh_screen(self):
        self.print_game_header()
        self.print_hangman_pic()

    def start(self):
        self.select_word()

        while self.remaining_attempts > 0:
            self.refresh_screen()
            letter = input('Enter a letter: ')

            self.user_chars.append(letter)

            if letter not in self.cleaned_word:
                self.failed_attempts += 1
                self.remaining_attempts -= 1

        self.refresh_screen()
        print(f'You lose. The word was: {self.word}')
