from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST','GET'])
def submit():
    if request.method == 'POST':
        name = request.form.get('name') # Get the name from the form
        marks = int(request.form.get('marks'))     
        return render_template('submit.html', name=name, marks=marks)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)