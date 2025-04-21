"""
Provide functions to print text in various colors using the 'termcolor' library.
Each function prints the given text in a specific color with reverse and blink attributes.
"""
from termcolor import colored


def print_green(text: str):
	print(colored(text, 'green', attrs=['reverse']), end='')


def print_yellow(text: str):
	print(colored(text, 'yellow', attrs=['reverse']), end='')


def print_red(text: str):
	print(colored(text, 'red', attrs=['reverse']), end='')


def print_congrats(text: str):
	print(colored(text, 'green', attrs=['reverse', 'blink']))


def print_lost(text: str):
	print(colored(text, 'red', attrs=['reverse', 'blink']))


def print_message(text: str):
	print(colored(text, 'white', attrs=['reverse']))
