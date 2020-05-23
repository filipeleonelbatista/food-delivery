from flask import Blueprint
pedidos = Blueprint('pedidos', __name__)
from . import routes