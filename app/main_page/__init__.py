from flask import Blueprint


main_page = Blueprint('main_page', __name__,)
from . import routes