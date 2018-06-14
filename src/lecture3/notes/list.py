import os # used for environment variables

from sqlalchemy import create_engine # create a database
from sqlalchemy.orm import scoped_session, sessionmaker # create a session for database

# sqlite://<nohostname>/<path>
# where <path> is relative:
engine = create_engine('sqlite:///lecture3.db') # create the engine
# engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine)) # bind engine to database

# create a database
def create_db():
    # TODO : autoincrement needed
    # Note: postgersql is not being used here, thus SERIAL has a different name
    db.execute('''
        CREATE TABLE flights
        (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          origin VARCHAR NOT NULL,
          destination VARCHAR NOT NULL,
          duration INTEGER NOT NULL
          );
    ''')
    db.commit()

# insert values into database and commit them     
def insert_db():
    vals = [
        "INSERT INTO flights \
        (origin, destination, duration) VALUES \
          ('Toronto', 'New York', 200);",
          
        "INSERT INTO flights \
          (origin, destination, duration) VALUES \
          ('Toronto', 'London', 1000);",
        
        "INSERT INTO flights \
          (origin, destination, duration) VALUES \
          ('New York', 'Toronto', 200);",
        
        "INSERT INTO FLIGHTS \
          (origin, destination, duration) VALUES \
          ('Vancouver', 'Toronto', 500);",
        
        "INSERT INTO flights \
          (origin, destination, duration) VALUES \
          ('New Deli', 'Bhagdad', 2000);",
        
        "INSERT INTO flights \
            (origin, destination, duration) VALUES \
            ('Peshawar', 'Toronto', 1000);",
        
        "INSERT INTO flights \
            (origin, destination, duration) VALUES  \
            ('Toronto', 'Peshawar', 1000);",
        
        "INSERT INTO FLIGHTS \
            (origin, destination, duration) VALUES \
            ('Vancouver', 'Peshawar', 1500);",
        
        "INSERT INTO flights \
            (origin, destination, duration) VALUES \
            ('New Deli', 'Peshawar', 450);"
        ]
    for val in vals:
        db.execute(val)
    db.commit()

# get the values and look at them 
def main():
    # print(db)
    
    flights = db.execute("SELECT id, origin, destination, duration FROM flights").fetchall()
    #fetchall() will give a list
    for fl in flights:
        print(f"{fl.id}: {fl.origin} to {fl.destination}, {fl.duration} min")

if __name__ == '__main__':
    main()
    # db.execute("DROP TABLE flights")
    # create_db()
    # insert_db()
    # db.execute("DELETE FROM flights WHERE id=3")
    # db.execute("INSERT INTO flights (origin, destination, duration) VALUES ('TEST', 'test2', 10)")
    # db.commit()
