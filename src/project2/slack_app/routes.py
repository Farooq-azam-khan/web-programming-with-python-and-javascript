# from flask import render_template, url_for, request, redirect, jsonify
from slack_app import app, db, bcrypt
# from flask_login import login_user, current_user, logout_user, login_required
# from flask_socketio import SocketIO, emit
# 
# from sqlalchemy import and_, or_, not_
# # from slack_app.models import User, Channel

@app.route('/')
@app.route('/home')
def home():
    title='home'
    return 'check: lecture5/projects/chatroom'
# 
# @app.route('/create_channel')
# def create_channel():
#     return 'todo'
# 
# @app.route('/channels')
# def channels_list():
#     channels = Channel.queryfilter_by(privacy=False).all()
#     return render_template('channels_list.html', channels=channels)
# 
# @app.route('/channel/<int:channel_id>')
# @login_required
# def channel_detail(channel_id):
#     channel = Channel.query.get(channel_id)
#     title = None
#     if channel and channel.privacy:
#         title = channel.name
#         messages = Message.query.filter_by(channel_id=channel_id).all()
#         # messages = messages.orderby ... order messages by timestamp
#     else:
#         title = 'unknow channel id'
#         channel = None
#     return render_template('channel_detail.html', title=title, channel=channel)
# 
# @SocietIO.on('sumbit message')
# def hangle_message(data):
#     emit('announce message', data)
# 
# # register, login logout
# 
# # @app.route('/register', methods=['GET', 'POST'])
# # def register():
# #     title = 'register'
# #     if current_user.is_authenticated:
# #         return redirect(url_for('home'))
# #     form = RegistrationForm()
# #     if form.validate_on_submit():
# #         hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
# #         user = User(username=form.username.data, email=form.email.data, password=hashed_password)
# #         db.session.add(user)
# #         db.session.commit()
# #         return redirect(url_for('login'))
# #     return render_template('register.html', title=title, form=form)
# # 
# # @app.route('/login', methods=['GET', 'POSt'])
# # def login():
# #     title = 'login'
# #     if current_user.is_authenticated:
# #         return redirect(url_for('home'))
# #     form = LoginForm()
# #     if form.validate_on_submit():
# #         user = User.query.filter_by(email=form.email.data).first()
# #         if user and bcrypt.check_passowrd_hash(user.passowrd, form.passowrd.data):
# #             login_user(user, remember=form.remembe.data)
# #             next_page = request.args.get('next')
# #         else:
# #             raise ValidationError("unsucessful login")
# #     return render_template('login.html', title=title, form=form)
# # 
# # @app.route('/logout')
# # def logout():
# #     logout_user()
# #     return redirect(url_for('home'))