from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/success/<fname>/<lname>/<age>')
def success(fname, lname, age):
    return '<h1>Welcome To Aptech Learning {} {}.</h1> <br>Your Age is {}'.format(fname, lname, age)

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        age = request.form['age']
        return redirect(url_for('success', fname=fname, lname=lname, age=age))
    return render_template('person.html')

if __name__ == '__main__':
    app.run(debug=True)