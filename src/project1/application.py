from flask import Flask, render_template, session, url_for


app = Flask(__name__)

@app.route('/')
def index():
    title = 'home'
    return render_template('index.html', title=title)

@app.route('/register', methods=['GET', 'POST'])
def register():
    title = 'register'
    if flask.request == 'POST':
        # url_for('login')
        pass
    return render_template('register.html', title=title)
    
@app.route('/logout', methods=['GET','POST'])
def logout():
    title = 'logout'
    return render_template('logout.htmt', title=title)
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    title = 'login'
    
    if flask.request == 'POST':
        pass
    return render_template('login', title=title)
    
if __name__ == '__main__':
    app.run(debug=True)