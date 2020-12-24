import os


class BaseConfig:
    base_dir = os.path.abspath(os.path.dirname(__file__))

    CSRF_ENABLE = True
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    ABS_UPLOAD_FOLDER = os.path.join(base_dir, 'app/static/uploads')
    REL_UPLOAD_FOLDER = 'static/uploads'
    # STATICFILES_DIRS = (os.path.join(base_dir, "static"))


class ProdConfig(BaseConfig):
    DEBUG = False

print(BaseConfig.base_dir)