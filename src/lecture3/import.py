import os
import csv

from sqlalchemy import create_engine # create a database
from sqlalchemy.orm import scoped_session, sessionmaker # create a session for database

engine = create_engine('sqlite:///lecture3.db') # create the engine
db = scoped_session(sessionmaker(bind=engine))


def select_db():
    flights = db.execute("SELECT origin, destination, duration FROM flights").fetchall()
    for fl in flights:
        print(f"flight {fl.origin} to {fl.destination} is {fl.duration} minutes long")
    
def main():
    f = open("flights.csv")
    print(f)
    reader = csv.reader(f)
    print(reader)
    for origin, destination, duration in reader:
        print("adding:", origin, destination, duration)
        # use placeholder variables as in :variable. 
        db.execute(f""" 
            INSERT INTO flights 
            (origin, destination, duration) VALUES 
            (:origin, :destination, :duration)
        """,
        {"origin":origin, 
        "destination":destination, 
        "duration":duration}
        )
    db.commit()
    f.close()
    
    
    
    
if __name__ == "__main__":
    main()
    select_db()