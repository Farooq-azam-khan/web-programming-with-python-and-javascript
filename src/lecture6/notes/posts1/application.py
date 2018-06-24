from flask import Flask, render_template, request, jsonify
import time 
app = Flask(__name__)

@app.route('/')
def index():
    print('rendering index.html')
    return render_template('index.html')

@app.route('/posts', methods=['POST'])
def posts(): 
    print('message to /post recieved')
    # get the start and end number of posts
    start = int(request.form.get('start') or 0)
    end = int(request.form.get('end') or (start+9))
    
    # genere list of posts
    data = []
    for i in range(start, end+1):
        data.append(f"Post #{i}")
        
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)