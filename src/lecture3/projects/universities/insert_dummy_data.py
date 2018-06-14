from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine('sqlite:///universities.db')
db = scoped_session(sessionmaker(bind=engine))


def insert_university():
    data = ["INSERT INTO universities (name, motto, location) VALUES ('Ryerson', 'some motto here', 1);",
            "INSERT INTO universities (name, motto, location) VALUES ('UofT', 'another motto here', 1);",
            "INSERT INTO universities (name, motto, location) VALUES ('McMasters', 'dummy text of a motto', 2);",
            "INSERT INTO universities (name, motto, location) VALUES ('Queens', 'no motto', 3);",
            "INSERT INTO universities (name, location) VALUES ('MiT', 4);",
            "INSERT INTO universities (name, location) VALUES ('Harvard', 4);",
            "INSERT INTO universities (name, location) VALUES ('Berkly', 4);",
    ]
    
    for d in data:
        db.execute(d)
    
    db.commit()
    print("inserted universities")

def insert_locations():
    data = ["INSERT INTO locations (name) VALUES ('Toronto');",
            "INSERT INTO locations (name) VALUES ('Quebec');",
            "INSERT INTO locations (name) VALUES ('Montreal');",
            "INSERT INTO locations (name) VALUES ('USA');",
    ]
    
    for d in data:
        db.execute(d)
    
    db.commit()
    print("inserted locations")

def insert_students():
    data = ["INSERT INTO students (f_name, l_name, email, uni_id) VALUES ('farooq', 'khan', 'f@ryerson.ca', 1);",
            "INSERT INTO students (f_name, l_name, email, uni_id) VALUES ('person a', 'person a lname', 'p@a.com', 2);",
            "INSERT INTO students (f_name, l_name, email, uni_id) VALUES ('person b', 'mike', 'mike@mcmaster.com', 3);",
            "INSERT INTO students (f_name, l_name, email, uni_id) VALUES ('abba', 'queen', 'abba.queen@queens.com', 3);",
            "INSERT INTO students (f_name, l_name, email, uni_id) VALUES ('far','mahmood', '@ryerson.ca.com.capital', '1');",
            "INSERT INTO students (f_name, l_name, email, uni_id) VALUES ('nash', 'alg', 'master@nashalg.com', 1);",
            "INSERT INTO students (f_name, l_name, email, uni_id) VALUES ('uni', 'guy', 'guy@uni.com', 4);",
    ]
    
    for d in data:
        db.execute(d)
    
    db.commit()
    print("inserted students")

def insert_courses():
    data = ["INSERT INTO courses (name, course_code, uni_id, professor_id) VALUES ('cs1', 'cps109', 1, 1);",
            "INSERT INTO courses (name, course_code, uni_id, professor_id) VALUES ('cs2', 'csp209', 2, 1);",
            "INSERT INTO courses (name, course_code, uni_id, professor_id) VALUES ('cs50', 'cs50', 6, 1);",
            "INSERT INTO courses (name, course_code, uni_id, professor_id) VALUES ('hard math real analysis', 'mth121', 2, 1);",
            "INSERT INTO courses (name, course_code, uni_id, professor_id) VALUES ('calc1', 'mth207', 1, 1);",
            "INSERT INTO courses (name, course_code, uni_id, professor_id) VALUES ('hmmmm.', 'eng101', 1, 1);",
            "INSERT INTO courses (name, course_code, uni_id, professor_id) VALUES ('not hmmm', 'phyl102', 2, 1);",
    ]
    
    for d in data:
        db.execute(d)
    
    db.commit()
    print("inserted courses")
    
def insert_professors():
    data = ["INSERT INTO professors (f_name, l_name, email, uni_id) VALUES ('tim', 'mcinerny', 'tim.mcinerny@ryerson.ca', 1);",
            "INSERT INTO professors (f_name, l_name, email, uni_id) VALUES ('ali', 'sadigen', 'ali.sadigen@ryerson.ca', 1);",
            "INSERT INTO professors (f_name, l_name, email, uni_id) VALUES ('ali', 'miri', 'ali.miri@ryerson.ca', 1);",
            "INSERT INTO professors (f_name, l_name, email, uni_id) VALUES ('saeid', 'samezadeh', 'saeid.samezadeh@ryerson.ca', 1);",
            "INSERT INTO professors (f_name, l_name, email, uni_id) VALUES ('david', 'milan', 'd.m@harvard.edu', 6);",
            "INSERT INTO professors (f_name, l_name, email, uni_id) VALUES ('crook', 'ception', 'c.c@uoft.ca', 6);",
            "INSERT INTO professors (f_name, l_name, email, uni_id) VALUES ('manny', 'potatoes', 'm.p@ryerson.ca', 6);",
    ]
    
    for d in data:
        db.execute(d)
    
    db.commit()
    print("inserted professors")


def insert_publications():
    data = ["INSERT INTO publications (title, content, professor) VALUES ('PUB1', 'This is some content for this publication.', 1);",
            "INSERT INTO publications (title, content, professor) VALUES ('PUB2', 'This is some content for this publication.', 1);",
            "INSERT INTO publications (title, content, professor) VALUES ('PUB3', 'This is some content for this publication.', 1);",
            "INSERT INTO publications (title, content, professor) VALUES ('PUB4', 'This is some content for this publication.', 1);",
            "INSERT INTO publications (title, content, professor) VALUES ('PUB5', 'This is some content for this publication.', 1);",
            "INSERT INTO publications (title, content, professor) VALUES ('PUB6', 'This is some content for this publication.', 1);",
            "INSERT INTO publications (title, content, professor) VALUES ('PUB7', 'This is some content for this publication.', 1);"
    ]

    for d in data:
        db.execute(d)

    db.commit()
    print("inserted publications")

if __name__ == '__main__':
    insert_locations()
    insert_university()
    insert_students()
    insert_courses()
    insert_publications()
    insert_professors()
    # pass
