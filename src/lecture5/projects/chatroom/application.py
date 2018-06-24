from flask import Flask, render_template, url_for, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdkilbill'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('submit message')
def handle_message(data):
    emit('announce message', data, broadcast=True)
    
if __name__ == '__main__':
    app.run(debug=True)
    socketio.ru(app)