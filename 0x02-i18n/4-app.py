#!/usr/bin/env python3
"""
A simple Flask web application with localization.
"""
from flask import Flask, render_template, request
from flask_babel import Babel, _

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


@babel.localeselector
def get_locale():
    """
    Determines the best language match based on
    the request's Accept-Language headers
    or locale parameter in the query string.
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Renders the index.html template with translated content.
    """

    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
