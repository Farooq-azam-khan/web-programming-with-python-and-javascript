from flask import Flask, render_template, request

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine('sqlite:///universities.db')
db = scoped_session(sessionmaker(bind=engine))

app = Flask(__name__)

@app.route('/')
@app.route('/universities')
def index():
    title = 'home'
    # display all the universities
    universities = db.execute("SELECT * FROM universities;").fetchall()
    return render_template('index.html', universities=universities, title=title)

@app.route('/courses')
def all_courses():
    title = 'courses'
    # display all the universities
    courses = db.execute("SELECT * FROM courses JOIN universities ON courses.uni_id=universities.id;").fetchall()
    return render_template('all_courses.html', courses=courses, title=title)

@app.route('/professors')
def all_professors():
    title = 'professors'
    # display all the universities
    professors = db.execute("SELECT * FROM professors JOIN universities ON professors.uni_id=universities.id;").fetchall()
    print(professors)
    return render_template('all_professors.html', professors=professors, title=title)
    
    
@app.route('/university/<string:university_name>')
def university(university_name):
    title = university_name
    # print("uni name:", title)
    university = db.execute("SELECT * FROM universities WHERE name=:name;", {'name':university_name}).fetchone()
    if university: 
        professors = db.execute("SELECT * FROM professors WHERE uni_id=:uni_id;", {'uni_id': university.id}).fetchall()
        courses = db.execute("SELECT * FROM courses WHERE uni_id=:uni_id;", {'uni_id':university.id}).fetchall()
    else:
        professors = []
        courses = []
        
    return render_template('university.html', professors=professors, courses=courses, university=university, title=title)
    
@app.route('/university/<string:university_name>/professors/')
def professors(university_name):
    title = 'professors at ' + university_name
    university = db.execute("SELECT * FROM universities WHERE name=:name;", {'name': university_name}).fetchone()
    professors = db.execute("SELECT * FROM professors WHERE id=:id;", {'id': university.id}).fetchall()
    return render_template('professors.html', professors=professors, title=title, university=university)
    
@app.route('/university/<string:university_name>/professors/<string:professor_name>')
def professor(university_name, professor_name):
    title = professor_name + 'at ' + university_name
    # fetch the university
    university = db.execute("SELECT * FROM universities WHERE name=:name;", {'name': university_name}).fetchone()
    professor = db.execute("SELECT * FROM professors WHERE uni_id=:uni_id AND l_name=:l_name", {'uni_id': university.id, 'l_name':professor_name}).fetchone()    
    courses = db.execute("SELECT * FROM courses WHERE professor_id=:professor_id", {'professor_id':professor.id})
    publications = db.execute('''
        SELECT * FROM publications WHERE professor=:professor_id;
    ''', {'professor_id':professor.id})
    return render_template('professor.html', publications=publications, courses=courses, title=title, professor=professor, university=university)
        
@app.route('/university/<string:university_name>/courses/')
def courses(university_name):
    title = 'courses at ' + university_name
    university = db.execute("SELECT * FROM universities WHERE name=:name;", {'name':university_name}).fetchone()
    courses = db.execute("SELECT * FROM courses WHERE uni_id=:uni_id;", {'uni_id':university.id}).fetchall()
    return render_template('courses.html', title=title)
    
@app.route('/university/<string:university_name>/courses/<string:course_code>')
def course(university_name, course_code):
    title = course_code + ' at ' + university_name
    university = db.execute("SELECT * FROM universities WHERE name=:name;", {'name':university_name}).fetchone()
    course = db.execute("SELECT * FROM courses WHERE uni_id=:uni_id AND course_code=:course_code;", {'uni_id':university.id, 'course_code':course_code}).fetchone()
    professor = db.execute("SELECT * FROM professors WHERE id=:course_id;", {'course_id':course.professor_id}).fetchone()
    return render_template('course.html', title=title, course=course, university=university, professor=professor)

@app.route('/professor/<string:professor_name>/publications/<int:publication_id>')
def publication(professor_name, publication_id):
    print(professor_name, "-"*10)
    professor = db.execute(''' 
        SELECT * FROM professors WHERE l_name=:name;
    ''', {'name':professor_name}).fetchone()
    publication = db.execute('''
        SELECT * FROM publications WHERE id=:id
    ''', {'id':publication_id}).fetchone()
    return render_template('publication.html', professor=professor, publication=publication)
    
if __name__ == '__main__':
    app.run(debug=True)