from flask import Flask
from flask_cors import CORS

from src.routes import *


def main() -> None:
    app = Flask(__name__)
    CORS(app)
    app.config["CORS_HEADERS"] = "Content-Type"
    app.register_blueprint(routes)
    app.run()


if __name__ == "__main__":
    main()
