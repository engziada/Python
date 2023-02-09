from flask import Blueprint,render_template,request,flash,redirect,url_for
from website.models import User,db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user ,login_required,logout_user,current_user

auth = Blueprint('auth', __name__)

@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method=="POST":
        email = request.form.get('email')
        password = request.form.get('password')

        if user := User.query.filter_by(email=email).first():
            if check_password_hash(user.password, password):
                if login_status := login_user(user, remember=True):
                    return redirect(url_for('views.home'))
                else:
                    flash("Logged in failed!", category="error")
            else:
                flash("Incorrect password",category="error")
        else:
            flash("User is not exists!","error")

    return render_template('login.html',user=current_user)


@auth.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))


@auth.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method=="POST":
        email = request.form.get('email')
        password = request.form.get('password')
        fullname=request.form.get('fullname')
        confirmpassword=request.form.get('confirmpassword')
        
        if user := User.query.filter_by(email=email).first():
            flash("User already exists!","error")    
        elif password!=confirmpassword:
            flash("Passwords not matching",category="error")
        else:
            new_user=User(email=email,password=generate_password_hash(password,method="sha256"),fullname=fullname)
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash("Account Created !", category="success")
            return redirect(url_for("views.home"))
        
    return render_template('signup.html',user=current_user)
