from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

text = ['<h1>First Page </h1> <p>This is text for the first page.</p>',
        '<h1>Second Page </h1> <p>This is text for the second page.</p>',
        '<h1>Third Page </h1> <p>This is text for the third page.</p>'
]
@app.route('/first')
def first():
    return text[0]

@app.route('/second')
def second():
    return text[1]
    
@app.route('/third')
def third():
    return text[2]
if __name__ == '__main__':
    app.run(debug=True)