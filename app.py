import os

from flask import Flask
from flask_cors import CORS

from src.routes import *


PORT = os.getenv("PORT", 5000)


def main() -> None:
    app = Flask(__name__)
    CORS(app)

    app.config["CORS_HEADERS"] = "Content-Type"
    app.register_blueprint(routes)
    app.run(port=PORT)


if __name__ == "__main__":
    main()
