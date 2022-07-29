import datetime
import os

SECRET_KEY = os.environ.get('SECRET_KEY')
SQLALCHEMY_DATABASE_URI = ""
SQLALCHEMY_TRACK_MODIFICATIONS = False

API_BASIC_URL = ""
JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
BCRYPT_LOG_ROUNDS = 5
JWT_QUERY_STRING_NAME = 'jwt'
JWT_TOKEN_LOCATION = ["query_string", "headers", "cookies", "json"]
JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(minutes=15)
JWT_REFRESH_TOKEN_EXPIRES = datetime.timedelta(days=7)
