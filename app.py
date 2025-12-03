from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    roll = request.form['roll']
    email = request.form['email']
    year = request.form['year']
    return render_template('result.html', name=name, roll=roll, email=email, year=year)

if __name__ == '__main__':
    app.run(debug=True)