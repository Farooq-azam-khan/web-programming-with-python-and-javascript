from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine('sqlite:///universities.db')
db = scoped_session(sessionmaker(bind=engine))

def select_university():
    db.execute('DROP TABLE universities;')

def select_student():
    pass

def select_courses():
    pass
    
def select_professors():
    pass

if __name__ == '__main__':
    select_university()
    # pass
