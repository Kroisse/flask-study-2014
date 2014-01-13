from flask import Flask

app = Flask(__name__)
from app import views  # not a good idea, but...
