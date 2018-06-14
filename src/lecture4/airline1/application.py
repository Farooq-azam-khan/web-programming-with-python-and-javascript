from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///..\\orm_flights.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Flight(db.Model):
    __tablename__ = "flights"
    id = db.Column(db.Integer, primary_key=True)
    origin = db.Column(db.String, nullable=False)
    destination = db.Column(db.String, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f'<Flight {self.origin} {self.destination}>'

class Passenger(db.Model):
    __tablename__ = "passengers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    flight_id = db.Column(db.Integer, db.ForeignKey("flights.id"), nullable=False)
    
    def __repr__(self):
        return f'<Passenger {self.id} {self.name}>'
    

@app.route("/")
@app.route("/flights")
def index():
    passengers = Passenger.query.all()
    flights = Flight.query.all()
    print(flights)
    # passengers = Passenger.query.all()
    return render_template("index.html", flights=flights, passengers=passengers)

@app.route("/book", methods=["POST", "GET"])
def book():
    ''' book a flight ''' 
    if request.method == "POST":
        name = request.form.get("name")
        try:
            flight_id = request.form.get("flight_id")
        except ValueError:
            return render_template("error.htlm", message="invaid flight number")
    
        # make sure flight exists
        flight = Flight.query.get(flight_id)
        if flight is None:
            return render_template("error.html", message="No such flight exist")
    
        # add passenger
        passenger = Passenger(name=name, flight_id=flight_id)
        db.session.add(passenger)
        db.session.commit()
    flights = Flight.query.all()
    return render_template("book.html", flights=flights)
    
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True)