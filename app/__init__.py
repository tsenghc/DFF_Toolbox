import logging
from logging.handlers import TimedRotatingFileHandler
from sys import prefix

from flask import Flask


def create_app():
    app = Flask(__name__,template_folder='template')
    app.config.from_pyfile('config.py')
    app.debug = True
    from app.main_page import main_page
    app.register_blueprint(main_page, prefix="/")

    return app
