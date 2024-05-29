#!/usr/bin/env python3
"""the py script for Basic Flask app """
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    """this method displays content from html files for the route """
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(debug=True)
