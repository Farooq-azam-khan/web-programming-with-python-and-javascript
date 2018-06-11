from flask import Flask, render_template, request, session
from flask_session import Session

from datetime import datetime
app = Flask(__name__)

# use seesions to keep data specific to user and not global
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

notes = [] # webserver stores variables 
@app.route("/", methods=["POST", "GET"])
def index():
    if session.get("notes") is None:
        session["notes"] = [] # this session will have empty list of notes
    if session.get("dates") is None: 
        session["dates"] = []
    if request.method == "POST":
        note = request.form.get("note")
        # notes.append(note)
        session["notes"].append(note)
        session["dates"].append(datetime.now())
        
    return render_template("index.html",iter_over=zip(session["notes"],session["dates"]))
if __name__ == "__main__":
    app.run(debug=True)