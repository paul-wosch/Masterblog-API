"""Provide the UI server."""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    """Provide the home route and return the index template."""
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
