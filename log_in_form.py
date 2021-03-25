from flask import *
from flask_bootstrap import Bootstrap
from flask_pymongo import PyMongo

app = Flask("address-book")
app.config['MONGO_URI' ] ="mongodb://localhost:27017/the-login-system-db"

Bootstrap(app)
mongo = PyMongo(app)

app.config['SECRET_KEY'] = 'sOmE_rAnDom_woRd'

@app.route('/', methods=['GET', 'POST'])
def Register():
    if request.method == 'GET':
        return render_template('Register.html')
    elif request.method == 'POST':
        doc={}
        for item in request.form:
            doc[item] = request.form[item]
    mongo.db.users.insert_one(doc)
    print(doc , "1111")
    flash('Account Created Successfully')
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        doc={'Email' : request.form['Email'], 'Password' : request.form['Password']}

        found = mongo.db.users.find_one(doc)
        print(doc)
        print(found)

        if found is None:
            flash('The email and Password you entered did not match our records. Please double checkand try again')

            return redirect('/login')
        else:
            session['user-info'] = {'firstName' : found['First_Name'], 'lastName' : found['Last_Name'], 'email': found['Email']}
            print('You entered')
            return redirect('/home')
@app.route('/home', methods=['GET', 'POST'])
def home():
    if 'user-info' in session:
        return render_template('home.html')
    else:
        flash('You need to login first')
        return redirect('/login')

app.run(debug=True)
