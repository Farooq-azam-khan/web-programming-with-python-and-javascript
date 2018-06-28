from flask import render_template, url_for, request, redirect
from book_app import app, db, bcrypt
from book_app.forms import RegistrationForm, LoginForm, SearchBookForm
from flask_login import login_user, current_user, logout_user, login_required

from sqlalchemy import and_, or_
# models 
from book_app.models import User, Book


@app.route('/', methods=['POST', 'GET'])
@app.route('/home', methods=['POST', 'GET'])
def home():
    title = 'home'
    
    form = SearchBookForm()
    books = None
    if form.validate_on_submit():
        search_data = form.search.data
        # Book.query.filter(Book.title.like('%'+search_data+'%')).all()
        search_like = '%'+search_data+'%'
        books = Book.query.filter(or_(Book.author.like(search_like), Book.title.like(search_like))).all()
    return render_template('index.html', title=title, form=form, books=books)

@app.route('/books')
def books():
    title = 'books'
    books = Book.query.all()
    return render_template('books.html', books=books, title=title)
    
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
    return render_template('account.html', title=title)

@app.route('/about')
def about():
    return "<h1> About Page </h1>"