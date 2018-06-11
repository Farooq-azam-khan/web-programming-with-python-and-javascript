from flask import Flask 

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello, World</h1>"
    
@app.route("/<string:name>")
def greet(name):
    name = name.capitalize()
    return f"<h1>Hello, <span style=\"color:green;\"> {name}</span></h1>"
    
if __name__ == "__main__":
    app.run(debug=True)