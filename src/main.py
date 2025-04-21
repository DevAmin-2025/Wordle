import json
import random

from src.utils import (print_congrats, print_green, print_lost, print_message,
                       print_red, print_yellow)

random.seed(42)

class Wordle:
    """
    A class to handle the game logic for a wordle game.

    :param file_path: The path to the word frequency file.

    Methods
    -------
    __init__(self, file_path):
        Initialize the game with the provided file.

    load_data(file_path):
        Read the word frequency json file and create a list of words with their frequency.

    process_data():
        Process the word list and return a list of 5-letter words sorted by frequency.

    create_random_word():
        Select a random word from the processed word list.

    ask_to_paly_again():
        Ask the user if they want to play again.

    play():
        Run the main game loop where the user guesses the word.
    """
    def __init__(self, file_path: str, word_length: int = 5, limit: int = 1000):
        self.word_length = word_length
        self.data = self.load_data(file_path)
        self.words = self.process_data(word_length, limit)
        self.random_word = self.create_random_word()

    def load_data(self, file_path):
        with open(file_path) as f:
            data = json.load(f)
        return data

    def process_data(self, word_length, limit) -> list:
        """
        Process the word list to select 5-letter words, sort them by frequency,
        limit to the top 1000 words, and remove the frequency information.

        :return: A list of 5-letter words sorted by frequency.
        """
        # Selecting 5-letter words
        self.data = [element for element in self.data if len(element[0]) == word_length]

        # Sorting frequency
        self.data = sorted(self.data, key=lambda x: x[1], reverse=True)

        # Selecting limited words
        self.data = self.data[:limit]

        # Removing frequency
        self.data = [element[0] for element in self.data]

        return self.data

    def create_random_word(self) -> str:
        """
        Generate a random word from self.words list.

        :return: A random word.
        """
        random_word = random.choice(self.words)
        return random_word

    def ask_to_play_again(self) -> str:
        """
        Ask the user if they want to play again.

        :return: The user's decision whether to play again.
        """
        play_again = input('Do you want to play again? (y/n): ').lower()
        return play_again

    def show_initial_map(self):
        for i in range(self.word_length):
            print_yellow(f' * ')
            print(' ', end='')
        print()

    def play(self):
        """
        Run the main game loop where the user guesses the word.

        The user is propmted to guess a 5-letter word and feedback is provided for each guess.
        The game continues until the user guesses the word correctly or runs out of guesses.
        """
        count_guess = 0
        initial_map_show_count = 0
        while True:
            if initial_map_show_count == 0:
                self.show_initial_map()
                initial_map_show_count += 1
            # Taking user guess
            user_guess = input(f'Enter a {self.word_length} letter word or (q to exit): ')
            user_guess = user_guess.lower()

            # Check if the user want to leave the game
            if user_guess == 'q':
                print_message('Goodbye')
                break
            # Check if user word is valid
            elif not user_guess.isalpha() or not len(user_guess) == self.word_length:
                print_message('Invalic input. Please try again.')
                continue
            # Check if user word is in the list of words
            elif not user_guess in set(self.words):
                print_message('Unknown word. Please try another word.')
                continue

            # Checking each letter of two words for position accuracy
            for uw, rw in zip(user_guess, self.random_word):
                if uw == rw:
                    print_green(f' {uw.upper()} ')
                    print(' ', end='')
                elif uw in self.random_word:
                    print_yellow(f' {uw.upper()} ')
                    print(' ', end='')
                else:
                    print_red(f' {uw.upper()} ')
                    print(' ', end='')

            print()
            # Adding one for each guess
            count_guess += 1

            # Congratulating user for the currect guess
            if user_guess == self.random_word:
                print()
                print_congrats('Congratulations! You win!')
                print()
                # Asking to play again
                play_again = self.ask_to_play_again()
                if play_again == 'y':
                    count_guess = 0
                    initial_map_show_count = 0
                    self.random_word = self.create_random_word()
                    continue
                else:
                    print_message('Goodbye')
                    break

            # Informing user that they lost
            if count_guess == 6:
                print()
                print_lost(f'Sorry! You ran out of guesses.')
                print_message(f'The word was:{self.random_word.title()}')
                print()
                # Asking to play again
                play_again = self.ask_to_play_again()
                if play_again.lower() == 'y':
                    initial_map_show_count = 0
                    count_guess = 0
                    self.random_word = self.create_random_word()
                    continue
                else:
                    print_message('Goodbye')
                    break


if __name__ == '__main__':
    file_path = 'data/words_frequency.json'
    wordle = Wordle(file_path)
    wordle.play()
