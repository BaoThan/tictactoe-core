import sys

from flask import Flask

from src.gui import run_gui
from src.routes import *


def main() -> None:
    if len(sys.argv) == 1:
        app = Flask(__name__)
        app.register_blueprint(routes)
        app.run()
    elif len(sys.argv) == 2 and sys.argv[1] in ("-g", "--gui"):
        sys.exit(run_gui())
    else:
        print("ERROR: Unknown options!")
        sys.exit(1)


if __name__ == "__main__":
    main()
