import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'docomin-thai-education-secret-key-2026')
    DATABASE = os.path.join(BASE_DIR, 'database', 'docomin.db')
    DEBUG = True
