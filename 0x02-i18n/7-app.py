#!/usr/bin/env python3
"""
A simple Flask web application with localization and user handling.
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _
import pytz
from pytz.exceptions import UnknownTimeZoneError

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

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """
    Retrieves the user based on the 'login_as' parameter in the query string.
    Returns a dictionary with user info or None if not found.
    """
    user_id = request.args.get('login_as')
    if user_id:
        return users.get(int(user_id))

    return None


@app.before_request
def before_request():
    """
    Runs before each request. Sets g.user to the user retrieved by get_user.
    """

    g.user = get_user()


@babel.localeselector
def get_locale():
    """
    Determines the best language match based on:
    - Locale parameter in the URL
    - User settings
    - Accept-Language headers
    - Default locale
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user['locale']

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """
    Determines the best timezone match based on:
    - Timezone parameter in the URL
    - User settings
    - Default timezone (UTC)
    """
    timezone = request.args.get('timezone')
    if timezone:
        try:
            pytz.timezone(timezone)
            return timezone
        except UnknownTimeZoneError:
            pass

    if g.user and g.user.get('timezone'):
        try:
            pytz.timezone(g.user['timezone'])
            return g.user['timezone']
        except UnknownTimeZoneError:
            pass

    return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/')
def index():
    """
    Renders the index.html template with translated content.
    """

    return render_template('7-index.html')


if __name__ == '__main__':
    app.run(debug=True)
