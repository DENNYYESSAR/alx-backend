#!/usr/bin/env python3
"""
Basic Flask app that serves a simple web page.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index() -> str:
    """
    Handles the root route by rendering an index.html template.

    Returns:
        str: The rendered HTML content for the root page.
    """
    return render_template('0-index.html')
