import os

from flask import Flask, request, render_template, session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

engine = create_engine('sqlite:///lecture3.db') # create the engine
# engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine)) # bind engine to database

@app.route("/", methods=["POST", "GET"])
def index():
    flights = db.execute("SELECT * FROM flights").fetchall()
    passengers = db.execute("SELECT * FROM passengers").fetchall()
    # print("flights:", flights)
    return render_template("index.html", flights=flights, passengers=passengers)

@app.route("/add_flight", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        origin = request.form.get("origin")
        destination = request.form.get("destination")
        duration = int(request.form.get("duration"))
        flight = {"origin":origin, "destination":destination, "duration":duration}
        # print(flight)
        db.execute("INSERT INTO flights (origin, destination, duration) VALUES (:origin, :destination, :duration)", 
        flight)
        print(flight)
    return render_template("add_flight.html")

@app.route("/book", methods=["POST", "GET"])
def book():
    if request.method == "POST":
        name = request.form.get("name")
        flight_code = request.form.get("flight_code")
        passenger = {"name":name, "flight_code":flight_code}
        print(passenger)
        # return render_template("error.html", message="error")
    
    if db.execute("SELECT * FROM flights WHERE id = :id", {"id":flight_code}).rowcount == 0:
        return render_template("error.html", message="no flight.")
    db.execute("INSERT INTO passengers (name, flight_code) VALUES (:name, :flight_code)", 
    passenger)
    flights = db.execute("SELECT * FROM flights").fetchall()
    return render_template("book_flight.html", flights=flights)
    
if __name__ =="__main__":
    app.run(debug=True)