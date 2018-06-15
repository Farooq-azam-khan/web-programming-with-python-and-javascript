from flask import Flask, request, render_template

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///airline2.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# models
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)
class Flight(db.Model):
    __tablename__ = "flights"
    id = db.Column(db.Integer, primary_key=True)
    origin = db.Column(db.String, nullable=False)
    destination = db.Column(db.String, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    
    def add_passenger(self, name):
        p = Passenger(name=name, flight_id=self.id)
        db.session.add(p)
        db.session.commit()
    
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
    return render_template("index.html", flights=flights, passengers=passengers)

@app.route('/flights/create', methods=['POST', 'GET'])
def create_flight():
    if request.method == 'POST':
        origin = request.form.get('origin')
        destination = request.form.get('destination')
        duration = int(request.form.get('duration'))
        db.session.add(Flight(origin=origin, duration=duration, destination=destination))
        db.session.commit()
    return render_template('create_flight.html')
@app.route("/flights/<int:flight_id>")
def flight(flight_id):
    flight = Flight.query.get(flight_id)
    print('flight:', flight)
    if flight is None:
        return render_template('error.html', message='Flight does not exists.')
        
    passengers = Passenger.query.filter_by(flight_id=flight_id).all()
    return render_template('flight.html', flight=flight, passengers=passengers)
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
            return render_template("error.html", message="No such flight exist.")
    
        # add passenger
        flight.add_passenger(name=name)
    flights = Flight.query.all()
    return render_template("book.html", flights=flights)
    
if __name__ == '__main__':
    with app.app_context():
        # db.create_all()
        app.run(debug=True)