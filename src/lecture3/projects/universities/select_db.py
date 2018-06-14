from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine('sqlite:///universities.db')
db = scoped_session(sessionmaker(bind=engine))

def select_university():
    universities = db.execute('''
        SELECT * FROM universities;
    ''').fetchall()
    
    print('-'*50)
    print("{:10s} selected universities".format(''))
    print('-'*50)
    for uni in universities:
        if uni.motto:
            print('{:3f} | {:10s} | {:20s}'.format(uni.id, uni.name, uni.motto))
        else:
            print('{:3f} | {:10s} | {:20s}'.format(uni.id, uni.name, ''))
    print('-'*50)
def select_student():
    students = db.execute('''
        SELECT * FROM students;
    ''').fetchall()
    
    print('-'*75)
    print("{:10s} selected stidents".format(''))
    print('-'*75)
    
    for s in students:
        print('{:3f}|{:10s}|{:20s}|{:25s}|{:3f}'.format(s.id, s.f_name, s.l_name, s.email, s.uni_id))
        
    print('-'*75)


def select_courses():
    courses = db.execute('''
        SELECT * FROM courses;
    ''').fetchall()
    
    print('-'*50)
    print("{:10s} selected courses".format(''))
    print('-'*50)
    
    for c in courses:
        print('{:3.0f} | {:25s} | {:.10s} | {:3.0f}'.format(c.id, c.name, c.course_code, c.uni_id))

    
def select_professors():
    professors = db.execute('''
        SELECT * FROM professors;
    ''').fetchall()
    
    print('-'*75)
    print("{:20s} selected professors".format(''))
    print('-'*75)
    
    for p in professors:
        print('{:3.0f} | {:10s} | {:10s} | {:28s} | {:3.0f} | {:3.0f}'.format(p.id, p.f_name, p.l_name, p.email, p.course, p.uni_id))


if __name__ == '__main__':
    # select_university()
    # select_student()
    # select_courses()
    select_professors()
