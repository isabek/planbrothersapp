# -*- coding: utf-8 -*-
import os


class Config(object):
    PROJECT = 'Bro'
    DEBUG = False
    PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


class DevelopConfig(Config):
    DEBUG = True
    ASSETS_DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = not True
