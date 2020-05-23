from flask import Blueprint
install = Blueprint('install', __name__)
from . import routes
