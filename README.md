# Snake Game - Multiple Levels

This project is a modern take on the classic Snake Game, implemented using Python and Pygame. The game features dynamic difficulty with multiple levels and progressively complex obstacle layouts that evolve as the player scores points. The core logic is contained in `snake_game.py`.

## Features

- Dynamic level progression based on player score
- Obstacles that increase in complexity with each level
- Food spawning logic that avoids snake and obstacle collisions
- Clean object-oriented design (`Snake`, `Food`)
- Fully covered by unit tests in `test_snake_game.py`

## Files

- `snake_game.py` – Main source file implementing the game logic
- `test_snake_game.py` – Comprehensive unit tests for snake movement, food placement, and obstacle logic
- `.gitignore` – Excludes Python cache, build artifacts, editor settings, and Pygame-related logs
- `README.md` – Detailed documentation of the project
- `LICENSE` – MIT License file

## Requirements

- Python 3.7+
- Pygame

## Install dependencies:

```bash```
pip install pygame


## How to Run

```bash```
python snake_game.py


## How to Test

```bash```
python -m unittest test_snake_game.py