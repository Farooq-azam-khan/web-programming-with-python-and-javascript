from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def index():
    headline = "Hello, variables"
    return render_template("index.html", headline=headline)
    
@app.route("/bye")
def bye():
    headline="bye"
    return render_template("index.html", headline=headline)

if __name__ == "__main__":
    app.run(debug=True)