import os


class BaseConfig:
    base_dir = os.path.abspath(os.path.dirname(__file__))
    CSRF_ENABLE = True
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    ABS_UPLOAD_FOLDER = os.path.join(base_dir, 'app/static/images/upload_img/')
    REL_UPLOAD_FOLDER = 'static/images/upload_img/'
    ABS_STYLIZED_FOLDER = os.path.join(base_dir, 'app/static/images/stylized_img/')
    REL_STYLIZED_FOLDER = 'static/images/stylized_img/'
    SEND_FILE_MAX_AGE_DEFAULT = 0


class ProdConfig(BaseConfig):
    DEBUG = False


print(BaseConfig.base_dir)
