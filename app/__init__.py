from flask import Flask
from config import BaseConfig


app = Flask(__name__, static_folder='./static')
app.config.from_object(BaseConfig)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

from app import views
