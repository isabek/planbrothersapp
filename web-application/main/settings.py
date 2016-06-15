# -*- coding: utf-8 -*-
import os


class Config(object):
    PROJECT = 'Bro'
    DEBUG = False
    PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    SQLALCHEMY_DATABASE_URI = 'postgresql://root:root@localhost:5432/bro_db'


class DevelopConfig(Config):
    DEBUG = True
    ASSETS_DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class HerokuConfig(Config):
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


config = {
    'default': Config,
    'development': DevelopConfig,
    'heroku': HerokuConfig
}