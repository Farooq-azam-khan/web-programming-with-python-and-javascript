from models import db, app, Flight

def main():
    flights = Flight.query.all()
    for flight in flights:
        print(f"{flight.origin} to {flight.destination} in {flight.duration} min")
    
if __name__ == '__main__':
    with app.app_context():
        main()