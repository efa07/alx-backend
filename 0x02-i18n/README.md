# Internationalization (i18n) with Flask
This repository contains a Flask web application demonstrating internationalization (i18n) using Flask-Babel. It provides examples of how to manage locales and time zones in a Flask application.

## Features
- Localization: Supports multiple languages (English and French).
- Time Zones: Handles different time zones based on user settings or URL parameters.
- User Management: Allows users to log in and see personalized messages.

## Setup
* 1.Clone the Repository:

```sh
git clone https://github.com/efa07/alx-backend.git
cd alx-backend/0x02-i18n
```
* 2.Install Dependencies:

Ensure you have Flask, Flask-Babel, and pytz installed. You can install the necessary packages using pip:

```sh
pip install Flask Flask-Babel pytz
```
* 3.Initialize Translations:

Extract messages, initialize translation files, and compile them:

```sh
Copy code
pybabel extract -F babel.cfg -o messages.pot .
pybabel init -i messages.pot -d translations -l en
pybabel init -i messages.pot -d translations -l fr
pybabel compile -d translations
```
* 4.Run the Application:

Start the Flask development server:

```sh
Copy code
python 0-app.py
```
Access the Application:

Open your web browser and go to http://127.0.0.1:5000/ to see the application in action.

## Usage
Localization: The application supports English and French. You can switch the language using URL parameters (e.g., ?locale=fr).
Time Zones: The current time is displayed based on the user's timezone, which can be set via URL parameters or user settings.
## License
This project is licensed under the MIT License - see the LICENSE file for details.
