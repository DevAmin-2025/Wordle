# Wrodle game

## Description
Wordle game is a python-based implemention of the popular word-guessing game. In this game, players try to guess a randomly selected five-letter word within six attempts.
The game provide feedback on each guess by highlighting letters that are correct and in the correct position (green), correct but in the wrong position (yellow), and incorrect (red). The game continues until the player guesses the word correctly or runs out of guesses.

## Code Overview
- `main.py`: Contains the game logic, including the `Wordle` class that handles the game flow, word selection and user interaction.
- `utils.py`: Provides utility functions for printing text in various colors using `termcolor` library.
- `README.md`: Documentation for the project, detailing its purpose, setup instructions, and usage guidelines.
- `requirements.txt`: Lists the dependecies to run the project.
- `.gitignore`: Specifies files and directories to exclude from version control, such as temporary files or environment-specific configurations.
- `LICENSE`: Includes the licensing information for the project, defining how it can be used or shared.
- `data/words_frequency.json`: A JSON file that stores word frequencies, for selecting words based on their frequency.
- `data/words_frequency.py`: The initial dataset from which `words_frequency.json` was created, containing raw word-frequency pairs.

## How to Run
Tor run the game, follow these steps:
1. **Clone the Repository**: Open your terminal and run the following command to clone the repository:
```bash
git clone https://github.com/your-username/your-repo.git
```
Replace your-username and your-repo with the actual GitHub username and repository name.

2. Navigate to the main project directory.
```bash
cd Wordle
```
3. Add the current directory to the `PYTHONPATH` and run the `main.py` script.
```bash
export PYTHONPATH=$PYTHONPATH:$(pwd)
python src/main.py
```
4. Install any necessary dependencies:
```bash
pip install -r requirements.txt
```
