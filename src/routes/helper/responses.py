from dataclasses import dataclass
from typing import Optional

from flask import jsonify
from flask import Response

from src.tictactoe_core import Player


@dataclass
class BestNextMoveResult:
    next_move: list[int]

    def to_flask_response(self) -> tuple[Response, int]:
        return (
            jsonify(
                {
                    "success": True,
                    "data": {
                        "next_move": self.next_move,
                    },
                }
            ),
            200,
        )


@dataclass
class BoardStatusResult:
    is_full: bool
    has_winner: bool
    winner: Optional[Player]

    def to_flask_response(self) -> tuple[Response, int]:
        return (
            jsonify(
                {
                    "success": True,
                    "data": {
                        "is_full": self.is_full,
                        "has_winner": self.has_winner,
                        "winner": self.winner.value if self.winner else None,
                    },
                }
            ),
            200,
        )


@dataclass
class FailureResult:
    error_message: str

    def to_flask_response(self) -> tuple[Response, int]:
        return jsonify({"success": False, "error_message": self.error_message}), 400
