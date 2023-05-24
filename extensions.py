from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from line_bot_api import line_bot_api

db = SQLAlchemy()
migrate = Migrate()


def get_line_bot_api():
    return line_bot_api
