import os


# Конфиг для фласка
class Config:
    base_dir = os.path.abspath(os.path.dirname(__file__))
    CSRF_ENABLE = True
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(base_dir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False