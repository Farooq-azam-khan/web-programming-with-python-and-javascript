from models import db, app, Flight
import csv 

def main():
    f = open('flights.csv')
    reader = csv.reader(f)
    for origin, destination, duration in reader:
        flight = Flight(origin=origin, destination=destination, duration=duration)
        db.session.add(flight)
    db.session.commit()
    f.close()

if __name__ == "__main__":
    with app.app_context():
        main()