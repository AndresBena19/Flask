import os

class Config(object):
    SECRET_KEY= 'KEY'

class DBconfig(Config):
    DEBUG =True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/hacked'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
