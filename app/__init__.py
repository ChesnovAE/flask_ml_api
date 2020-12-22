from flask import Flask
from config import BaseConfig


app = Flask(__name__, static_folder='./static')
app.config.from_object(BaseConfig)

from app import views