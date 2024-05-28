#!/usr/bin/env python3
from application import app, babel
from flask import render_template, request
from application.babel_c import Config
"""contains routes"""


@babel.localeselector
def get_locale():
    """this function get locales"""
    return request.accept_languages.best_match(Config().LANGUANGES)

@app.route('/')
def home():
    """returns an index"""
    return render_template('0-index.html')

# @app.route('/')
# def home():
#     """returns an index"""
#     return render_template('1-index.html')

# @app.route('/')
# def home():
#     """returns an index"""
#     return render_template('2-index.html')


