from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("sqlite:///..\\lecture3.db")
db = scoped_session(sessionmaker(bind=engine))
def select_table():
    fs = db.execute("SELECT * FROM flights;")
    ps = db.execute("SELECT * FROM passengers")
    
    for f in fs:
        print ("o: {} d: {} du:{}".format(f.origin, f.destination, f.duration))
    for p in ps:
        print("n: {} fc :{}".format(p.name, p.flight_code))
        
if __name__ == "__main__":
    select_table()
    