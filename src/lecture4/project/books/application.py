from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# TODO: remove the author_id=1 and add the proper code of any author
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']  = 'sqlite:///publications.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# class User(db.Model):
#     __tablename__ = 'users'
#     id = db.Column(db.String, primary_key=True)
#     name = db.Column(db.String, nullable=False)
#     email = db.Column(db.String, nullable=False, unique=True)
#     reviews = db.relationship('Review', backref='users', lazy=True)
# 
#     # TODO: to be implemented
#     def create_user(self, name, email):
#         user = User(name=name, email=email)
#         db.session.add(user)
#         db.session.commit()
# 
#     def update_user(self, id, name, email):
#         user = User.query.get(id)
#         user.name = name
#         user.email = email
#         db.session.commit()
# 
#     def delete_user(self, id):
#         user = User.query.get(id)
#         db.session.delete(user)
#         db.session.commit()

class Review(db.Model):
    # TODO: associate review with user later
    # user_id = db.Column(db.Integer, db.FoerignKey('users.id', nullable=False))
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    
    def add(self, book_id, title, content, rating):
        review = Review(
                        book_id=book_id, 
                        title=title,
                        content=content,
                        rating=rating
                        )
        db.session.add(review)
        db.session.commit()
        
    def check_rating(self, rating):
        return rating > 10 and rating < 0
    
    def update(self, id, title, content, rating):
        review = Review.query.get(id)
        review.title = title
        review.content = content
        review.rating = rating
        db.session.commit()
    
    def delete_review(self, id):
        review = Review.query.get(id)
        db.session.delete(review)
        db.session.commit()
    
    def __repr__(self):
        return f'<Review {self.title}>'
        

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
    
    def add_review(self, title, content, rating):
        review = Review(title=title, book_id=self.id, content=content, rating=rating)
        db.session.add(review)
        db.session.commit()
    
    def __repr__(self):
        return f'<Book {self.title}>'
    
class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)
    f_name  = db.Column(db.String, nullable=False)
    l_name  = db.Column(db.String, nullable=False)
    email   = db.Column(db.String, nullable=True)
    bio     = db.Column(db.String, nullable=True)
    books   = db.relationship('Book', backref='author', lazy=True)
    
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
        return f'<Author {self.f_name} {self.l_name}>'

@app.route('/')
def index():
    authors = Author.query.all()
    books = Book.query.all()
    reviews = Review.query.all()
    return render_template('index.html', authors=authors, books=books, reviews=reviews)

@app.route('/register')    
def register():
    return '<h1> not yet implemented </h1>'

@app.route('/login')
@app.route('/signin')
def login():
    return '<h1> not yet implemented </h1>'

@app.route('/signup')
def signup():
    return '<h1> not yet implemented </h1>'
    
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
    reviews = Review.query.filter_by(book_id=book_id).all()
    print("review:", reviews)
    return render_template('book_detail.html', book=book, reviews=reviews)

@app.route('/books/<int:book_id>/reviews')
def book_reviews(book_id):
    book = Book.query.get(book_id)
    reviews = Review.query.filter_by(book_id=book_id).all()
    return render_template('reviews_list.html', reviews=reviews, book=book)
    
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


@app.route('/reviews')
def reviews_list():
    books = Book.query.all()
    reviews = Review.query.all()
    return render_template('all_reviews_list.html', reviews=reviews, books=books)

@app.route('/reviews/create', methods=['POST', 'GET'])
def create_review():
    
    books = Book.query.all()
    
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        rating = int(request.form.get('rating'))
        
        if rating >10 and rating < 0:
            render_template('error.html', message='rating must be between 0 and 10')
        book_id = request.form.get('book_id')
        book = Book.query.get(book_id)
        book.add_review(title=title, content=content, rating=rating)
        
    return render_template('create_review.html', books=books)


@app.route('/reviews/<int:review_id>/update', methods=['POST', 'GET'])
def update_review(review_id):
    review = Review.query.get(review_id)
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        rating = int(request.form.get('rating'))
        
        if rating > 10 and rating < 0:
            return render_template('error.html', message='invalid rating.')
        
        review.update(id=review.id, title=title, content=content, rating=rating)
    return render_template('update_review.html', review=review)

@app.route('/reviews/<int:review_id>/delete')
def delete_review(review_id):
    return '<h1> to be implemented </h1>'
    
# TODO: Implement your own api (jsonify)
@app.route('/api')
def api():
    books = Book.query.all()
    books_l = []
    for book in books: 
        author = Author.query.get(book.author_id)
        books_l.append({
            'title':book.title,
            'subtitle':book.subtitle,
            'publisher':book.publisher,
            'year_published': book.year_published,
            'author': {
                    'f_name': author.f_name,
                    'l_name':author.l_name,
                    'email': author.email
            }
        
        })
    
    authors = Author.query.all()
    authors_l = []    
    for author in authors:
        a_books = author.books
        a_books_l = []
        for a_book in a_books:
            a_books_l.append({
                            'title':book.title,
                            'subtitle':book.subtitle,
                            'publisher':book.publisher,
                            'year_published': book.year_published
            })
            
        authors_l.append({
                        'f_name': author.f_name,
                        'l_name':author.l_name,
                        'email': author.email,
                        'books': a_books_l
        })
        
    reviews = Review.query.all()
    reviews_l = []
    for review in reviews:
        r_book = Book.query.get(review.book_id)
        reviews_l.append({
                        'title': review.title,
                        'content': review.content,
                        'rating': review.rating,
                        'book': {
                            'title':r_book.title,
                            'subtitle':r_book.subtitle,
                            'publisher':r_book.publisher,
                            'year_published': r_book.year_published
                        }
        })
    return jsonify({'books':books_l, 'authors': authors_l, 'reviews':reviews_l})
    
@app.route('/api/users')
def api_users():
    return 'to be implemented: will return list of users'

@app.route('/api/users/<string:user_email>')
def api_user(user_email):
    return 'to be implemented'

@app.route('/api/users/<string:user_email>/reviews')
def api_user_reviews(user_email):
    return 'to be implemented: return list of review of user'

@app.route('/api/users/<string:user_email>/review/<int:review_id>')
def api_user_review(user_email, review_id):
    return 'to be implemented: return user\'s particular review'

@app.route('/api/reviews')
def api_reviews():
    reviews = Review.query.all()
    reviews_l = []
    for review in reviews:
        r_book = Book.query.get(review.book_id)
        reviews_l.append({
                        'title': review.title,
                        'content': review.content,
                        'rating': review.rating,
                        'book': {
                            'title':r_book.title,
                            'subtitle':r_book.subtitle,
                            'publisher':r_book.publisher,
                            'year_published': r_book.year_published
                        }
        })
    return jsonify({'reviews':reviews_l})
    
@app.route('/api/reviews/<int:review_id>')
def api_review(review_id):
    review = Review.query.get(review_id)
    
    if review is None:
        return jsonity({ 'error': 'No such review'}), 422
    book = Book.query.get(review.book_id)
    author = Author.query.get(book.author_id)
    
    return jsonify({
                    'title': review.title,
                    'content': review.content,
                    'rating': review.rating,
                    'book': {
                            'title': book.title,
                            'subtitle': book.subtitle,
                            'summary': book.summary,
                            'author': {
                                    'f_name': author.f_name,
                                    'l_name': author.l_name,
                                    'email': author.email
                            }
                    }
                })
    
@app.route('/api/authors')
def api_authors():
    return 'TODO: return authors'

@app.route('/api/books')
def api_books():
    return 'todo: return books'
    
# more api links 
'''
/api/authors/<int:author_id>/books
/api/authors/<int:author_id>/books/<int:book_id>
/api/authors/<int:author_id>/books/<int:book_id>/reviews
/api/books/<int:book_id>
/api/books/<int:book_id>/reviews
...
'''

if __name__ == '__main__':
    with app.app_context():
        # db.create_all()
        app.run(debug=True)