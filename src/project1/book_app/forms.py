from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
# models
from book_app.models import User


class ReviewForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    content = StringField('explination', validators=[DataRequired()])
    rating = IntegerField('rating', validators=None)
    submit = SubmitField('write')
    
class SearchBookForm(FlaskForm):
    search = StringField('book info', validators=[DataRequired(), Length(min=2)])
    submit = SubmitField('search')
    
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken.')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField('Login')