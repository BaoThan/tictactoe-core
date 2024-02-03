from . import routes


@routes.route("/", methods=["HEAD", "GET"])
def index():
    return "hello from tictactoe-core"
