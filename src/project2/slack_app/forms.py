from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, SubmitField, BooleanField
from wtform.validators import DataRequired, Length, Email, EqualTo, ValidationError


class Message(FlaskForm):
    # user will be the current login in user
    # channel will be the channel id at the url 
    content = StringField('message', validators=[DataRequired()])
    
class SearchChannelForm(FlaskForm):
    name = StringField('channel name', validators=[DataRequired()])
    
class CreateChannelForm(FlaskForm):
    name = StringField('channel name', validators=[DataRequired()])
    private = BooleanField('is Private channel')
    
class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Passowrd', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')