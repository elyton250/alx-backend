#!/usr/bin/env python3
from flask import Flask
from flask_babel import Babel
"""this is a flask app we are goint to us babel"""


app = Flask(__name__)
babel = Babel(app)

from application.babel_c import Config
app.config.from_object(Config)


from application import routes
