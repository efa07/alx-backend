#!/usr/bin/env python3
"""
A simple Flask web application with localization.
"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """
    Configuration class for Flask-Babel.
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)

babel = Babel(app)


@app.route('/')
def index():
    """
    Renders the 0-index.html template.
    """

    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
