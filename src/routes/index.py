from . import routes


@routes.route("/")
def index():
    return "hello from tictactoe-core"
