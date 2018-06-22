from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    title = 'home | get exchange rate'
    return render_template('index.html', title=title)

@app.route('/convert', methods=['POST'])
def convert():
    # get dummy data
    currency = request.form.get('currency')
    res = 1 #one dollar
    # if False: #!= 200
    #     return jsonify({"success":False})
    
    data = {'rate':res}#res.json()
    # if currency not in data['rates']:
    #     return jsonify('success':False)
    return jsonify({'success':True, "rate":data})
    
    
    
    
if __name__ == '__main__':
    app.run(debug=True)