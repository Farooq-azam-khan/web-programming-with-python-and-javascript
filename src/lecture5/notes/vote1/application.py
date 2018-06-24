from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a;lkdfjalk'
socketio = SocketIO(app)


# sotre in database here
votes = {'yes':0, 'no':0, 'maybe':0}

@app.route('/')
def index():
    title = 'home'
    return render_template('index.html', title=title, votes=votes)

@socketio.on('submit vote')
def vote(data):
    selection = data["selection"]
    votes[selection] += 1
    emit('vote totals', votes, broadcast=True)


if __name__ == '__main__':
    app.run(debug=True)
    socketio.run(app)