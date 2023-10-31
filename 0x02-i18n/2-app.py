#!/usr/bin/env python3
"""setting up python flask environent"""
from flask import Flask, render_template, request
from flask_babel import Babel  # type: ignore


app = Flask(__name__)


class Config:
    '''
    configuration for default values
    '''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    '''
    get the locale language
    '''
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', )
def index():
    """The index page being setting up"""
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run(port=5000)
