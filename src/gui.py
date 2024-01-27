from PyQt6.QtCore import QPointF
from PyQt6.QtCore import QRectF
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QGraphicsItem
from PyQt6.QtWidgets import QGraphicsScene
from PyQt6.QtWidgets import QGraphicsView
from PyQt6.QtWidgets import QMessageBox

from src.tictactoe_core import best_next_move
from src.tictactoe_core import check_winner
from src.tictactoe_core import is_board_full
from src.tictactoe_core import is_board_valid
from src.tictactoe_core import Player

EMPTY = ""
SIZE = 3


class TicTacToe(QGraphicsItem):
    def __init__(self):
        super().__init__()
        self.O = "O"
        self.X = "X"
        self.player_mark = "O"
        self.bot_mark = "X"
        self._reset()

    def boundingRect(self):
        return QRectF(0, 0, 300, 300)

    def select(self, x, y):
        if self.board[y][x] != EMPTY:
            return

        self.board[y][x] = self.player_mark
        if not self._check_board():
            return

        self._let_bot_move()
        if not self._check_board():
            return

    def paint(self, painter, option, widget):
        _ = option  # ignore option param
        _ = widget  # ignore widget param
        painter.drawLine(0, 100, 300, 100)
        painter.drawLine(0, 200, 300, 200)
        painter.drawLine(100, 0, 100, 300)
        painter.drawLine(200, 0, 200, 300)
        for y in range(SIZE):
            for x in range(SIZE):
                if self.board[y][x] == self.O:
                    painter.drawEllipse(QPointF(50 + x * 100, 50 + y * 100), 35, 35)
                elif self.board[y][x] == self.X:
                    painter.drawLine(
                        20 + x * 100, 20 + y * 100, 80 + x * 100, 80 + y * 100
                    )
                    painter.drawLine(
                        20 + x * 100, 80 + y * 100, 80 + x * 100, 20 + y * 100
                    )

    def mousePressEvent(self, event):
        self.select(int(event.pos().x() / 100), int(event.pos().y() / 100))
        self.update()

    def _show_game_over_dialog(self, title: str, msg: str) -> None:
        dlg = QMessageBox()
        dlg.setWindowTitle(title)
        dlg.setText(msg)
        dlg.exec()
        self._reset()

    def _reset(self) -> None:
        self.board = [
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
        ]
        self.board[1][1] = self.bot_mark

    def _let_bot_move(self) -> None:
        x, y = best_next_move(self.board, Player(self.bot_mark))
        print(f"Bot made a move at slot ({x}, {y})")

        if self.board[x][y] != EMPTY:
            print(f"ERROR: Slot ({x}, {y}) is not empty")
            return
        self.board[x][y] = self.bot_mark

    def _check_board(self) -> bool:
        if not is_board_valid(self.board):
            self._show_game_over_dialog("Error", "Something went wrong!")
            return False

        winner = check_winner(self.board)
        if winner is not None:
            self._show_game_over_dialog("Game Over", f"{winner.value} wins!")
            return False
        if is_board_full(self.board):
            self._show_game_over_dialog("Game Over", "Tie!")
            return False

        return True


class MainWindow(QGraphicsView):
    def __init__(self):
        super().__init__()
        scene = QGraphicsScene(self)
        self.tictactoe = TicTacToe()
        scene.addItem(self.tictactoe)
        scene.setSceneRect(0, 0, 300, 300)
        self.setScene(scene)
        self.show()


def run_gui() -> int:
    app = QApplication([])
    win = MainWindow()
    win.show()
    return app.exec()
