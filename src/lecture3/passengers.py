import os
import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session 

engine = create_engine('sqlite:///lecture3.db')
db = scoped_session(sessionmaker(bind=engine))

def create_passenger_db():
    # TODO: autoincrement needed for id
    db.execute("""
        CREATE TABLE passengers
        (
            id INTEGER UNIQUE PRIMARY KEY,
            name VARCHAR NOT NULL, 
            flight_code INTEGER REFERENCES flights
        );
    """)
    db.commit()
    
def insert_passengers_db():
    passengers = [
        "INSERT INTO passengers \
            (name, flight_code) VALUES ('Khan', 10);",
        "INSERT INTO passengers \
            (name, flight_code) VALUES ('Potato', 3);",
        "INSERT INTO passengers \
            (name, flight_code) VALUES ('Ed', 5);", 
        "INSERT INTO passengers \
            (name, flight_code) VALUES ('Samantha', 6);",
        "INSERT INTO passengers \
            (name, flight_code) VALUES ('Tomato', 8);",
        "INSERT INTO passengers \
            (name, flight_code) VALUES ('Jon', 10);", 
        "INSERT INTO passengers \
            (name, flight_code) VALUES ('Eddy', 3);",
        "INSERT INTO passengers \
            (name, flight_code) VALUES ('Sally', 12);",
        "INSERT INTO passengers \
            (name, flight_code) VALUES ('Pam', 10);", 
        "INSERT INTO passengers \
            (name, flight_code) VALUES ('Jim', 13);",
        "INSERT INTO passengers \
            (name, flight_code) VALUES ('Dwight', 4);",
        "INSERT INTO passengers \
            (name, flight_code) VALUES ('Office Mike', 3);", 
        "INSERT INTO passengers \
            (name, flight_code) VALUES ('Prison Mike', 3);",
        "INSERT INTO passengers \
            (name, flight_code) VALUES ('Sal', 4);",
        "INSERT INTO passengers \
            (name, flight_code) VALUES ('Walter', 4);"     
    ]
    
    for passenger in passengers:
        db.execute(passenger)
    db.commit()

def select_passenger_db():
    flights = db.execute("""
        SELECT id, origin, destination, duration
        FROM  flights
    """).fetchall()
    
    for flight in flights:
        print(f"{flight.id}: {flight.origin} to {flight.destination} in {flight.duration}")
    
    flight_id = int(input("\nF-ID: "))
    flight = db.execute("SELECT origin, destination, duration FROM flights WHERE id=:id",
    {"id": flight_id})
    print("flight:", flight)
    
    if flight is None:
        print("error, give valid fid")
        return 
    
    
    passenger = db.execute("""
        SELECT name FROM passengers WHERE flight_code = :flight_id
        """, {"flight_id":flight_id}).fetchall()
    print(passenger)
    

if __name__ == "__main__":

    # db.execute("DROP TABLE passengers")
    # create_passenger_db()
    insert_passengers_db()
    select_passenger_db()