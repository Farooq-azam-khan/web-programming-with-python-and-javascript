from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

# TODO: remove the author_id=1 and add the proper code of any author
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']  = 'sqlite:///publications.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# TODO: create database
class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    subtitle = db.Column(db.String, nullable=True)
    summary = db.Column(db.String, nullable=True)
    publisher = db.Column(db.String, nullable=True)
    year_published = db.Column(db.Integer, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)
    
    def __repr__(self):
        return f'<Book {self.title}'
    
class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String, nullable=False)
    l_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=True)
    books = db.relationship('Book', backref='author', lazy=True)
    
    def add_book(self, title, year_published, subtitle='', summary='', publisher=''):
        b = Book(title=title, 
                year_published=year_published, 
                subtitle=subtitle, 
                summary=summary, 
                publisher=publisher, 
                author=self.id)
        db.session.add(b)
        db.session.commit()
            
    def __repr__(self):
        return f'<Author {self.f_name} {self.l_name}'

@app.route('/')
def index():
    authors = Author.query.all()
    books = Book.query.all()
    return render_template('index.html', authors=authors, books=books)
    
@app.route('/books')
def books_list():
    books = Book.query.all()
    return render_template('book_list.html', books=books)

@app.route('/books/create', methods=["POST", "GET"])
def create_book():
    if request.method == 'POST':
        title           = request.form.get('title')
        subtitle        = request.form.get('subtitle')
        summary         = request.form.get('summary')
        publisher       = request.form.get('publisher')
        year_published  = int(request.form.get('year_published'))
        author_id         = request.form.get('author_id')
        book = Book(title=title, 
                subtitle=subtitle, 
                summary=summary, 
                publisher=publisher, 
                year_published=year_published, 
                author_id=author_id)
        db.session.add(book)
        db.session.commit()
    authors = Author.query.all()
    return render_template('create_book.html', authors=authors)

@app.route('/books/<int:book_id>')
def book_detail(book_id):
    book = Book.query.get(book_id)
    return render_template('book_detail.html', book=book)
    
@app.route('/books/<int:book_id>/update', methods=['POST', 'GET'])
def update_book(book_id):
    
    book = Book.query.get(book_id)
    authors = Author.query.all()
    if request.method == 'POST':
        title           = request.form.get('title')
        subtitle        = request.form.get('subtitle')
        summary         = request.form.get('summary')
        publisher       = request.form.get('publisher')
        year_published  = int(request.form.get('year_published'))
        author_id         = request.form.get('author_id')
        book.title = title
        book.subtitle = subtitle 
        book.publisher = publisher
        book.year_published = year_published
        book.author_id = author_id
        db.session.commit()
    return render_template('update_book.html', book=book, authors=authors)

@app.route('/authors')
def authors_list():
    authors = Author.query.all()
    return render_template('author_list.html', authors=authors)

@app.route('/authors/<int:author_id>')
def author_detail(author_id):
    author = Author.query.get(author_id)
    return render_template('author_detail.html', author=author)
    
    
@app.route('/authors/create', methods=['POST', 'GET'])
def create_author():
    if request.method == 'POST':
        f_name = request.form.get('f_name')
        l_name = request.form.get('l_name')
        email = request.form.get('email')
        author = Author(f_name=f_name, l_name=l_name,email=email)
        db.session.add(author)
        db.session.commit()
    return render_template('create_author.html')
    

@app.route('/authors/<int:author_id>/update', methods=['POST', 'GET'])
def update_author(author_id):
    
    author = Author.query.get(author_id)
    if request.method == 'POST':
        f_name = request.form.get('f_name')
        l_name = request.form.get('l_name')
        email = request.form.get('email')
        # update information
        author.f_name = f_name
        author.l_name = l_name
        author.email = email
        db.session.commit()
    return render_template('update_author.html', author=author)

if __name__ == '__main__':
    with app.app_context():
        # db.create_all()
        app.run(debug=True)