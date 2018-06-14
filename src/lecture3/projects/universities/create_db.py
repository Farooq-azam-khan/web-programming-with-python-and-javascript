from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine('sqlite:///universities.db')
db = scoped_session(sessionmaker(bind=engine))

def create_university():
    db.execute('''
    CREATE TABLE universities (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        name VARCHAR UNIQUE NOT NULL,
        motto VARCHAR UNIQUE, 
        location INTEGER REFERENCES locations(id)
    );
    ''')
    print("created university table")

def create_student():
    # TODO: students have to be enrolled in courses    
    # again many to many relation is needed 
    db.execute('''
        CREATE TABLE students(
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            f_name VARCHAR NOT NULL,
            l_name VARCHAR NOT NULL, 
            email VARCHAR UNIQUE NOT NULL,
            uni_id INTEGER REFERENCES universities(id)
        );
    ''')
    
    print("created student table")

def create_courses():
    db.execute('''
        CREATE TABLE courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR,
            course_code VARCHAR UNIQUE NOT NULL,
            uni_id INTEGER REFERENCES universities(id),
            professor_id INTEGER REFERENCES professors(id)         
        );
    ''')
    
    print("created courses table")
    
    
def create_professors():
    # TODO: make it so that the professors can teach more than one course (many to many field)
    # need an intermediate table for that 
    db.execute('''
        CREATE TABLE professors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            f_name VARCHAR NOT NULL,
            l_name VARCHAR NOT NULL,
            email VARCHAR UNIQUE NOT NULL,
            uni_id INTEGER REFERENCES universities(id)
        );
    ''')
    
    print("created professors table")


def create_location():
    # database of locations, 
    # check where students live, university campuses are, and professors addresses
    db.execute('''
        CREATE TABLE locations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR NOT NULL
        );
    ''')
    
    
def create_publication():
    db.execute('''
        CREATE TABLE publications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title VARCHAR NOT NULL,
            content VARCHAR NOT NULL, 
            professor INTEGER REFERENCES professors(id)
        );
    ''')
    # create table for university and its publications and the professors associated with it
    
def create_departmnet():
    # create department for each university and the professors that are in that department
    # also have field for department head
    db.execute('''
        CREATE TABLE departments (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name VARCHAR NOT NULL, 
        );
    ''')
    
if __name__ == '__main__':
    create_university()
    create_student()
    create_courses()
    create_professors()
    create_publication()
    create_location()