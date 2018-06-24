from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit 
import requests 

app = Flask(__name__)
# generate secret key
app.config['SECRET_KEY'] = 'aslkdjfals342dkfjasdkfjalsdfjpoweifad'

# initalize socket (emiting and receiving data)
socketio = SocketIO(app)

@app.route('/')
def index():
    title = 'home'
    return render_template('index.html', title=title)

@socketio.on('submit vote')
def vote(data):
    emit('announce vote', data, broadcast=True)

if __name__ == '__main__':
    app.run(debug=True)
    socketio.run(app)