from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# "GET" is method not allowed
@app.route("/hello_old", methods=["POST"])
def hello_old():
    print("request:", request)
    print("request.form:", request.form)
    name = request.form.get("name")
    return render_template("hello.html", name=name)

@app.route("/hello", methods=["POST", "GET"])
def hello():
    if request.method == "GET":
        return "go from home"
    elif request.method == "POST":
        name = request.form.get("name")
    return render_template("hello.html", name=name)
    
if __name__ == "__main__":
    app.run(debug=True)