from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/first')
def index():
    return render_template('index.html', title='first page')
    
@app.route('/second')    
def second():
    return render_template('second.html', title='second page')
    
@app.route('/third')
def third():
    return render_template('third.html', title='third page')
    
if __name__ == '__main__':
    app.run(debug=True)