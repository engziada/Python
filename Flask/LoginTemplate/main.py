from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
from flask_bootstrap import Bootstrap
from werkzeug.security import generate_password_hash, check_password_hash
import re

# Create FLASK application
app = Flask(__name__)
app.config["SECRET_KEY"] ="12qwaszx#E"

# Create bootstrap
Bootstrap(app)

# MySQL database configuration parameters
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "P@ssw0rd1234567"
app.config["MYSQL_DB"] = "dating"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"
db = MySQL(app)



def create_admin():
    admin_email = 'admin@here.com'
    admin_password = generate_password_hash('admin', method="sha256")
    admin_fullname = 'Administrator'
    try:
        cursor = db.connection.cursor()
        
        #check if admin is already registered
        cursor.execute(f"SELECT * FROM user WHERE email = '{admin_email}'")
        result = cursor.fetchone()
        if result:
            print('Administrator account already exists.')
        else:
            cursor.execute(f"INSERT INTO user (fullname, password, email) VALUES('{admin_fullname}', '{admin_password}', '{admin_email}')")
            db.connection.commit()
            code = cursor.lastrowid
            print(f'Administrator account created successfully with record id: {code}')
    except Exception as e:
        print(e)




@app.route('/login/', methods=['GET', 'POST'])
def login():
    check_db_connection(db)

    # Output message if something goes wrong...
    msg = ''
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        # Create variables for easy access
        email = request.form['email']
        password = request.form['password']
        
        # Check if account exists using MySQL
        cursor = db.connection.cursor()
        cursor.execute(f"SELECT * FROM user WHERE email = '{email}'")
        account = cursor.fetchone()
        
        # If account exists in accounts table in out database
        if account:
            # Check for password
            if check_password_hash(account['password'], password):
                # Create session data, we can access this data in other routes
                session['loggedin'] = True
                session['iduser'] = account['iduser']
                session['email'] = account['email']
                session['fullname'] = account['fullname']
                # Redirect to home page
                return redirect(url_for('home'))
            else:
                # Password incorrect
                msg = 'Incorrect password!'
        else:
            # Account doesnt exist
            msg = "Account doesn't exist!"
    return render_template('index.html', msg=msg)




@app.route('/logout')
def logout():
    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   session.pop('iduser', None)
   session.pop('email', None)
   session.pop('fullname', None)
   # Redirect to login page
   return redirect(url_for('login'))




@app.route('/register', methods=['GET', 'POST'])
def register():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'fullname' in request.form and 'password' in request.form and 'email' in request.form:
        # Create variables for easy access
        fullname = request.form['fullname']
        password = generate_password_hash(
            request.form['password'], method="sha256")
        email = request.form['email']
        # Check if account exists using MySQL
        cursor = db.connection.cursor()
        cursor.execute(f"SELECT * FROM user WHERE fullname = '{fullname}'")
        account = cursor.fetchone()
        # If account exists show error and validation checks
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not fullname or not password or not email:
            msg = 'Please fill out the form!'
        else:
            # Account doesnt exists and the form data is valid, now insert new account into accounts table
            cursor.execute(f"INSERT INTO user (email,fullname,password) VALUES ('{email}','{fullname}','{password}')")
            db.connection.commit()
            msg = 'You have successfully registered!'
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('register.html', msg=msg)




@app.route('/')
@app.route('/home')
def home():
    # Check if user is loggedin
    if 'loggedin' in session:
        # User is loggedin show them the home page
        return render_template('home.html', fullname=session['fullname'])
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))




@app.route('/profile')
def profile():
    # Check if user is loggedin
    if 'loggedin' in session:
        # We need all the account info for the user so we can display it on the profile page
        cursor = db.connection.cursor()
        cursor.execute(f"SELECT * FROM user WHERE iduser = '{session['iduser']}'")
        account = cursor.fetchone()
        # Show the profile page with account info
        return render_template('profile.html', account=account)
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))




def check_db_connection(database):
    # Check if database connection established
    if database.connection:
        print('Database connection established successfully.')
        # Create administrator account
        create_admin()
    else:
        print('Database connection failed!')   
        exit(-1) 

if __name__ == '__main__':
    app.run(debug=True)

    
