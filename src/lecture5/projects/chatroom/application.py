from flask import Flask, render_template, url_for, request
from flask_socketio import SocketIO, emit


messages = []

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdkilbill'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html', title='home', messages=messages)

@socketio.on('submit message')
def handle_message(data):
    messages.append(data)
    # print("data:", data)
    emit('announce message', data, broadcast=True)
    
if __name__ == '__main__':
    app.run(debug=True)
    socketio.run(app)