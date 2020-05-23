from flask import Blueprint
estoque = Blueprint('estoque', __name__)
from . import routes