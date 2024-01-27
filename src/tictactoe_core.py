"""
This file contains the core functionality for the Tic Tac Toe game.
"""
from enum import Enum
from typing import Optional

BOARD_SIZE = 3

_BOT_WINS_POINT = 1
_HUMAN_WINS_POINT = -1
_TIE_POINT = 0


class Player(Enum):
    X = "X"
    O = "O"


def is_board_full(board: list[list[str]]) -> bool:
    """
    Check if the game board is full and no other move can be made.

    Returns:
        True if the game board is full, False otherwise.
    """
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] == "":
                return False
    return True


def check_winner(board: list[list[str]]) -> Optional[Player]:
    """
    Check if there is a winner for the given game board.
    Returns:
        None if there is no winner, otherwise returns the winning Player.
    """
    # Check rows:
    for i in range(BOARD_SIZE):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return Player(board[i][0].upper())

    # Check cols:
    for j in range(BOARD_SIZE):
        if board[0][j] == board[1][j] == board[2][j] != "":
            return Player(board[0][j].upper())

    # check diagonals:
    if board[0][0] == board[1][1] == board[2][2] != "":
        return Player(board[0][0].upper())
    if board[0][2] == board[1][1] == board[2][0] != "":
        return Player(board[0][2].upper())

    return None


def is_board_valid(board: list[list[str]]) -> bool:
    """
    Check if a given input board is valid.

    Returns:
        True if the game board is valid, False otherwise.
    """
    # check if board has 3x3 dimensions:
    if len(board) != BOARD_SIZE:
        return False
    for i in range(BOARD_SIZE):
        if len(board[i]) != BOARD_SIZE:
            return False

    # check the input should be x/X/o/O only:
    VALID_MOVE = {"x", "X", "o", "O", ""}

    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j].strip() not in VALID_MOVE:
                return False

    count_x = 0
    count_o = 0
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] == "x" or board[i][j] == "X":
                count_x += 1
            if board[i][j] == "o" or board[i][j] == "O":
                count_o += 1

    return False if abs(count_x - count_o) > 1 else True


def best_next_move(board: list[list[str]], for_player: Player) -> list[int]:
    best_score = float("-inf")
    best_move = [-1, -1]

    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j].strip():
                continue

            board[i][j] = for_player.value
            score = _minimax(board, for_player, False)

            if score > best_score:
                best_score = score
                best_move = [i, j]
            board[i][j] = ""

    return best_move


def _minimax(board: list[list[str]], for_player: Player, maximizing: bool) -> int:
    best_score = float("-inf") if maximizing else float("inf")
    bot_move = for_player
    human_move = Player.X if bot_move == Player.O else Player.O

    if check_winner(board) == bot_move:
        return _BOT_WINS_POINT
    if check_winner(board) == human_move:
        return _HUMAN_WINS_POINT
    if is_board_full(board):
        return _TIE_POINT

    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j].strip():
                continue

            board[i][j] = bot_move.value if maximizing else human_move.value
            score = _minimax(board, bot_move, not maximizing)
            best_score = (
                max(score, best_score) if maximizing else min(score, best_score)
            )
            board[i][j] = ""

    return best_score
