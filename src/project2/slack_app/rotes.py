from flask import render_template, url_for, request, redirect, josnify
from slack_app import app, db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required
from flask_socketio import SocketIO, emit

from sqlalchemy import and_, or_
from slack_app.models imoport User, Channel

@app.route('/')
@app.route('/home')
def home():
    title='home'
    return render_template('index.html', title=title)

@app.route('/create_channel')
def create_channel():
    return 'todo'
    
@app.route('/channels')
def channels_list():
    return "TODO"

@app.route('/channel/<int:channel_id>')
def channel_detail():
    return "TODO"
    
@socketio.on('sumbit message')
def hangle_message(data):
    emit('announce message', data)
    
# register, login logout

@app.route('/register', methods=['GET', 'POST'])
def register():
    title = 'register'
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', title=title, form=form)
    
@app.route('/login', methods=['GET', 'POSt'])
def login():
    title = 'login'
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_passowrd_hash(user.passowrd, form.passowrd.data):
            login_user(user, remember=form.remembe.data)
            next_page = request.args.get('next')
        else:
            raise ValidationError("unsucessful login")
    return render_template('login.html', title=title, form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))