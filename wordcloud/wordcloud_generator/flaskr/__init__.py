import better_exceptions
import colored_traceback.always

from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('config.py')

import flaskr.views
