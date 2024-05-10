from enum import Enum

import os
import random
import sys

class Player(Enum):
    X = "X"
    O = "O"

class State(Enum):
    PLAYING = "PLAYING"
    X_WIN = "X_WIN"
    O_WIN = "O_WIN"
    STALEMATE = "STALEMATE"


def main():
    # Initialize the game board.
    board = [[" ", " ", " "] for _ in range(3)]

    # Initialize the player's moves.
    x_moves = []
    o_moves = []

    # Initialize the game's state.
    state = State.PLAYING

    # Play the game until it ends.
    while state == State.PLAYING:
        # Display the game board.
        display_board(board)

        # Prompt the player to make a move.
        player = Player.X if len(x_moves) == len(o_moves) else Player.O
        move = input(f"{player}'s turn: Enter a row and column (e.g., 1 2): ")

        # Parse and validate the player's move.
        row, column = move.split()
        row = int(row) - 1
        column = int(column) - 1
        if not (0 <= row < 3 and 0 <= column < 3 and board[row][column] == " "):
            print("Invalid move. Please try again.")
            continue

        # Add the player's move to the game board.
        if player == Player.X:
            x_moves.append((row, column))
        else:
            o_moves.append((row, column))
        board[row][column] = player.value

        # Check if the player has won or lost the game.
        state = validate_win(board, player.value)

    # Display the winner or stalemate message.
    if state == State.X_WIN:
        print("X wins!")
    elif state == State.O_WIN:
        print("O wins!")
    else:
        print("Stalemate!")

    # Reset the game.
    board = [[" ", " ", " "] for _ in range(3)]
    x_moves = []
    o_moves = []
    state = State.PLAYING


def display_board(board):
    for row in board:
        for cell in row:
            print(cell, end=" ")
        print()


def validate_win(board, player):
    # Check the rows.
    for row in board:
        if all(cell == player for cell in row):
            return State.X_WIN if player == "X" else State.O_WIN

    # Check the columns.
    for column in range(3):
        if all(board[row][column] == player for row in range(3)):
            return State.X_WIN if player == "X" else State.O_WIN

    # Check the diagonals.
    if all(board[i][i] == player for i in range(3)):
        return State.X_WIN if player == "X" else State.O_WIN
    if all(board[2-i][i] == player for i in range(3)):
        return State.X_WIN if player == "X" else State.O_WIN

    # Check for a stalemate.
    if all(cell != " " for cell in board[0]) and all(cell != " " for cell in board[1]) and all(cell != " " for cell in board[2]):
        return State.STALEMATE

    # The game is still playing.
    return State.PLAYING


if __name__ == "__main__":
    main()