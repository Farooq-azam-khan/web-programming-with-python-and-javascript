import os

from flask import Flask, request, render_template, session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker 

app = Flask(__name__)

engine = create_engine('sqlite:///..\\lecture3.db')
db = scoped_session(sessionmaker(bind=engine)) # bind engine to database

@app.route("/")
def index():
    flights = db.execute("SELECT * FROM flights").fetchall()
    passengers = db.execute("SELECT * FROM passengers").fetchall()
    return render_template("index.html", flights=flights, passengers=passengers)

@app.route("/add_flight", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        flight = {  'origin':request.form.get('origin'),
                    'destination':request.form.get('destination'),
                    'duration':request.form.get('duration')
                }
        # TODO:add to database
    return render_template("add_flight.html")

@app.route("/book", methods=["POST", "GET"])
def book():
    flights = db.execute("SELECT * FROM flights;")
    if request.method == "POST":
        passenger = {'name':request.form.get('name'),
                    'flight_id':request.form.get('flight_id')
                    }
        # TODO:add to databse, getting some error                    
        # db.execute("SELECT * FROM passengers").fetchone()
        # db.execute("INSERT INTO passengers (name, flight_code) VALUES ('khan', 1)")
        # db.commit()
    return render_template("book_flight.html", flights=flights)
    
if __name__ =="__main__":
    app.run(debug=True)