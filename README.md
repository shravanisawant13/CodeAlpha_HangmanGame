# 🎮 CodeAlpha Hangman Game

A simple **text-based Hangman Game** developed in Python as part of the **CodeAlpha Python Programming Internship**.

## 📌 Project Overview

This project is a console-based word guessing game. The computer randomly selects one word from a list of five predefined words, and the player tries to guess the word one letter at a time.

The player is allowed a maximum of **6 incorrect guesses**.

## ✨ Features

- 🎲 Random selection of a secret word
- 📝 Five predefined words
- 🔤 Hidden letters displayed using underscores
- ✅ Input validation
- 🔎 Correct letters are revealed in their proper positions
- 🚫 Prevents repeated guesses
- ❌ Maximum of 6 incorrect guesses
- 🏆 Win condition
- 💀 Game-over condition
- 💻 Simple console-based interface

## 🛠️ Technologies Used

- Python 3
- `random` module
- Lists
- Strings
- `while` loop
- `if-elif-else` conditions
- User input

## 📂 Project Structure

```text
CodeAlpha_HangmanGame/
│
├── hangman.py
├── README.md
└── screenshots/
    └── hangman_output.png
```

## ▶️ How to Run

### 1. Install Python

Make sure **Python 3** is installed on your computer.

### 2. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/CodeAlpha_HangmanGame.git
```

### 3. Open the Project Folder

```bash
cd CodeAlpha_HangmanGame
```

### 4. Run the Program

```bash
python hangman.py
```

## 🎯 How to Play

1. Run the program.
2. The computer randomly selects a secret word.
3. Enter one letter at a time.
4. If the letter is correct, it will be displayed in the word.
5. If the letter is incorrect, the incorrect guess count increases.
6. You have a maximum of **6 incorrect guesses**.
7. Reveal all the letters to win the game.
8. If you use all 6 incorrect guesses, the game ends.

## 💻 Example Output

```text
Welcome to Hangman!
Guess the secret word.
_ _ _ _ _ _

Enter a letter: p
Correct guess!
Word: p _ _ _ _ _

Enter a letter: z
Wrong guess!
Incorrect guesses: 1 / 6
Word: p _ _ _ _ _
```

## 📚 Learning Outcomes

Through this project, I practiced:

- Python programming fundamentals
- Lists and strings
- Random selection
- Loops and conditional statements
- User input validation
- Handling repeated inputs
- Basic problem-solving and game logic

## 🎓 Internship

This project was developed as part of the **CodeAlpha Python Programming Internship**.

## 👩‍💻 Author

**Shravani**

Aspiring Data Analyst | Python | Data Analytics
