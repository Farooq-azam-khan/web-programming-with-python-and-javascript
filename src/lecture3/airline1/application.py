from flask import Flask, request, render_template, session

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")