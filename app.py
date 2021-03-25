from flask import *
from flask_bootstrap import Bootstrap
from flask_pymongo import PyMongo


@app.route('/',methods=['POST','GET'])
def registration():
    return render_template('registration.html')

@app.route('/registeruser', methods=['POST', 'GET'])
def user():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    users = {}
    users[email] = {'first_name': f, 'last_name': l, 'email': email, 'password': p}
    return "Name: {first_name} {last_name} and Email {email}".format(first_name=first_name, last_name=last_name, email=email)

app.run(debug=True)
