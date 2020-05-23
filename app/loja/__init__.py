from flask import Blueprint
loja = Blueprint('loja', __name__)
from . import routes
