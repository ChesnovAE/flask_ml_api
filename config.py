import os


class BaseConfig:
    base_dir = os.path.abspath(os.path.dirname(__file__))

    CSRF_ENABLE = True
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    UPLOAD_FOLDER = os.path.join(base_dir, 'loads')


class ProdConfig(BaseConfig):
    DEBUG = False