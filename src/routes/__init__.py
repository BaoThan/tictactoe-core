from flask import Blueprint

routes = Blueprint("routes", __name__)

from .index import *
from .best_next_move import *
from .board_status import *
