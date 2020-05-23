from flask import Blueprint
usuarios = Blueprint('usuarios', __name__)
from . import routes