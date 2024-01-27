import json

from flask import request

from . import routes
from src.routes.helper.responses import BoardStatusResult
from src.routes.helper.responses import FailureResult
from src.tictactoe_core import check_winner
from src.tictactoe_core import is_board_full
from src.tictactoe_core import is_board_valid


@routes.route("/board_status", methods=["POST"])
def board_status():
    """
    board_status REST API, support POST requests only.
    This API will take in a 2D array as the representation of the tic tac toe
    board, and will return a result of the board status (including whether the
    board is full, whether there is a winner, and if there is a winner then
    who is the winner). In case the tic tac toe board is invalid, it will return
    an error message along with response code of 400
    """
    board = json.loads(request.form["board"])
    board_valid = is_board_valid(board)

    if not board_valid:
        return FailureResult("Invalid board").to_flask_response()

    winner = check_winner(board)
    has_winner = winner is not None
    return BoardStatusResult(
        is_board_full(board), has_winner, winner
    ).to_flask_response()
