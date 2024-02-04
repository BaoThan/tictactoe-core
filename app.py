from flask import Flask

from src.routes import *


def main() -> None:
    app = Flask(__name__)
    app.register_blueprint(routes)
    app.run()


if __name__ == "__main__":
    main()
