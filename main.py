"""
This module is designed to initialise the Flask web application. 
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", method=["GET"])
def index():
    return render_template("index.html")

@app.route("/about", method=["GET"])
def about():
    return render_template("about.html")

@app.route("/services", method=["GET"])
def services():
    return render_template("services.html")

@app.route("/contact", method=["GET"])
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)