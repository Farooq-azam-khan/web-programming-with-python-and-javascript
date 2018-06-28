from datetime import datetime
from book_app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.Integer, unique=True)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    publication_year = db.Column(db.String, nullable=False)
    averate_rating = db.Column(db.Integer, nullable=True)
    publisher = db.Column(db.String, nullable=True)
    
    def to_dict(self):
        return {
        "id": self.id,
        "isbn": self.isbn,
        "title": self.title, 
        "author": self.author, 
        'publication_year': self.publication_year,
        "publisher": self.publisher
        }

class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    
class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    
    def __repr__(self):
        return f"User< {self.username} {self.id}>"
