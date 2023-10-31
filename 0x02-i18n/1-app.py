#!/usr/bin/env python3
"""setting up python flask environent"""
from flask import Flask, render_template
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


@app.route('/', )
def index():
    """The index page being setting up"""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(port=5000)
