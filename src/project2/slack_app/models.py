from datetime import datetime
from slack_app import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class UserModel(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=False)
    username = db.Column(db.String, unique=True, nullalble=False)
    email = db.Column(db.String, unique=True, nullalbe=False)
    password = db.Column(db.String, nullalbe=Flase)
    
    def __repr__(self):
        return f"<User {self.username}>"
    
    
class ChannelModel(db.Model):
    __tablename__ = 'channels'
    name = db.Column(db.String, unique=True, nullable=False)
    id = db.Column(db.Integer, primary_key=True)
    users = db.relationship('UserModel', backref='channel', lazy=True)
    private = db.Column(db.Boolean, default=True, nullalbe=True)
    creator_user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullalbe=False)
    
class MessageModel(db.Model):
    __tablename__ = 'messages'
    content = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullalbe=False)
    channel_id = db.Column(db.Integer, db.ForeignKey('channels.id'), nullalbe=False)
    # timestamp = db.Column(db.Integer, db.) get time stamp