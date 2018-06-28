from flask import render_template, url_for, request, redirect, jsonify
from book_app import app, db, bcrypt
from book_app.forms import RegistrationForm, LoginForm, SearchBookForm, ReviewForm
from flask_login import login_user, current_user, logout_user, login_required

from sqlalchemy import and_, or_
# models 
from book_app.models import User, Book, Review


@app.route('/', methods=['POST', 'GET'])
@app.route('/home', methods=['POST', 'GET'])
def home():
    title = 'home'
    form = SearchBookForm()
    books = None
    if form.validate_on_submit():
        search_data = form.search.data
        print('search_data:', form.search)
        # Book.query.filter(Book.title.like('%'+search_data+'%')).all()
        search_like = '%'+search_data+'%'
        books = Book.query.filter(or_(Book.author.like(search_like), Book.title.like(search_like))).all()

    return render_template('index.html', title=title, form=form)

@app.route('/search', methods=['POST'])
def search():
    search_data = request.form.get('search_query')
    print('data:', search_data)
    search_like = '%'+search_data+'%'
    books = Book.query.filter(or_(Book.author.like(search_like), Book.title.like(search_like))).all()
    print(books)
    books_json = []
    for book in books: 
        book_json = {
            "id": book.id, 
            "title": book.title, 
            "isbn": book.isbn, 
            "author": book.author
        }
        books_json.append(book_json)
    data = {'books':books_json}
    return jsonify(data)

@app.route('/books')
def books():
    title = 'books'
    books = Book.query.all()
    return render_template('books.html', books=books, title=title)

@app.route('/book/<int:book_id>', methods=['GET'])
def book(book_id):
    book = Book.query.get(book_id)
    if book: 
        title = 'book ' + str(book.title)
        reviews = Review.query.filter_by(book_id=book.id)
    return render_template('book_detail.html', title=title, book=book, reviews=reviews)

@app.route('/register', methods=['GET', 'POST'])
def register():
    title = 'register'
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        # print('valid form', '-'*50)
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', title=title, form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    title = 'login'
    
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            print('unsuccesful login')
    return render_template('login.html', title=title, form=form)
    
    
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/account')
@login_required
def account():
    title = 'Account'
    reviews = Review.query.filter_by(user_id=current_user.id)
    return render_template('account.html', title=title, reviews=reviews)

@app.route('/about')
def about():
    return "<h1> About Page </h1>"
    
@app.route('/create_review/<int:book_id>', methods=['POST', 'GET'])
@login_required
def create_review(book_id):
    form = ReviewForm()
    book = Book.query.get(book_id)
    if form.validate_on_submit():
        print(form.title.data)
        review = Review(user_id=current_user.id, 
                        book_id=book.id, title=form.title.data, 
                        content=form.content.data, 
                        rating=form.rating.data)
        print(form.title.data)
        print(form.content.data)
        print(form.rating.data)
        print(review)
        db.session.add(review)
        db.session.commit()
        return redirect(url_for('book', book_id=book.id))
    return render_template('create_review.html', book_id=book_id, book=book, form=form)

    
@app.route('/api/isbn/<int:book_isbn>')
def api_book_isbn(book_isbn):
    book = Book.query.filter_by(isbn=book_isbn).first()
    data = None
    if book:
        book = book.to_dict()
        data = {'book':book}
    else:
        data = {'book':None}
    return jsonify(data)