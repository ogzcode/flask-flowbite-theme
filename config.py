import os
from datetime import timedelta


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=5)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    """ SQLALCHEMY_ECHO = True
    SQLALCHEMY_RECORD_QUERIES = True """
