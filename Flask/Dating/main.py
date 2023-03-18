from flask_bootstrap import Bootstrap5
from flask import Flask, render_template, request, redirect, url_for, session, make_response,flash
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from whatsapp import WhatsApp
import pandas as pd
import io,re,csv,string
from random import choices

# Create FLASK application
app = Flask(__name__)
app.config["SECRET_KEY"] ="12qwaszx#E"

# MySQL database configuration parameters
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "P@ssw0rd1234567"
app.config["MYSQL_DB"] = "dating"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

# app.config["MYSQL_HOST"] = "ziada.mysql.pythonanywhere-services.com"
# app.config["MYSQL_USER"] = "ziada"
# app.config["MYSQL_PASSWORD"] = "P@ssw0rd1234567"
# app.config["MYSQL_DB"] = "ziada$dating"
# app.config["MYSQL_CURSORCLASS"] = "DictCursor"

# Initialize Bootstrap
bootstrap = Bootstrap5(app)

# Initialize Database
db = MySQL(app)

def checkPassword(username:str,password:str)->int:
    phoneno=username
    cursor = db.connection.cursor()
    cursor.execute(f"SELECT * FROM user WHERE phoneno = '{phoneno}'")
    account = cursor.fetchone()
    
    # If account exists in accounts table in out database
    if account:
        # Check for password
        if check_password_hash(account['password'], password):
            return 0
        else:
            return -1
    else:
        return -2


def updatePassword(username: str, password: str):
    phoneno = username
    newhashedpassword = generate_password_hash(password, method="sha256")
    cursor = db.connection.cursor()
    cursor.execute(
        f"Update user SET password='{newhashedpassword}' WHERE phoneno='{phoneno}'")
    db.connection.commit()



@app.route('/login/', methods=['GET', 'POST'])
def login():
    check_db_connection(db)

    # Output message if something goes wrong...
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST':
        # Create variables for easy access
        phoneno = request.form.get('phoneno')
        password = request.form.get('password')

        if 'login' in request.form and phoneno and password:
        # 'phoneno' in request.form and 'password' in request.form:
            # Check if account exists using MySQL

            cursor = db.connection.cursor()
            cursor.execute(f"SELECT * FROM user WHERE phoneno = '{phoneno}'")
            account = cursor.fetchone()

            # If account exists in accounts table in out database
            retcode=checkPassword(phoneno,password)
            if retcode==-2: #No Account
                flash("المستخدم غير موجود")
            elif retcode==-1: #Incorrect Password
                flash('كلمة المرور غير صحيحة')
            elif retcode==0: #Correct password
                # Create session data, we can access this data in other routes
                session['loggedin'] = True
                session['userid'] = account['iduser']
                session['phoneno'] = account['phoneno']
                session['fullname'] = account['fullname']
                print(session)

                # Redirect to home page
                return redirect(url_for('home'))

        elif 'forgetpassword' in request.form:
            forgetpassword(request.form.get('targetphoneno'))
    return render_template('index.html')




@app.route('/logout')
def logout():
    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   session.pop('userid', None)
   session.pop('phoneno', None)
   session.pop('fullname', None)
   # Redirect to login page
   return redirect(url_for('login'))




@app.route('/register', methods=['GET', 'POST'])
def register():
    # Output message if something goes wrong...
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'fullname' in request.form and 'password' in request.form and 'phoneno' in request.form:
        # Create variables for easy access
        fullname = request.form['fullname']
        password = generate_password_hash(
            request.form['password'], method="sha256")
        phoneno = request.form['phoneno']

        # Check if account exists using MySQL
        cursor = db.connection.cursor()
        cursor.execute(f"SELECT * FROM user WHERE phoneno = '{phoneno}'")
        accountbyphone = cursor.fetchone()
        # If account exists show error and validation checks
        if accountbyphone:
            flash('رقم الجوال موجود بالفعل')
        elif not fullname or not password or not phoneno:
            flash('من فضلك أكمل البيانات')
        else:
            # Account doesnt exists and the form data is valid, now insert new account into accounts table
            cursor.execute(f"INSERT INTO user (fullname,phoneno,password) VALUES ('{fullname}','{phoneno}','{password}')")
            db.connection.commit()
            flash('تم التسجيل بنجاح')
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        flash('من فضلك أكمل البيانات')
    # Show registration form with message (if any)
    return render_template('register.html')




@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    # Check if user is loggedin
    if 'loggedin' in session:
        if request.method == 'POST':
            #In case of Search button pressed
            if "Search" in request.form:
                ageMin = request.form.get('ageMin')
                ageMax = request.form.get('ageMax')
                lengthMin = request.form.get('lengthMin')
                lengthMax = request.form.get('lengthMax')
                weightMin = request.form.get('weightMin')
                weightMax = request.form.get('weightMax')
                smokingstatus = request.form.get('smokingstatus')
                marriagetype = request.form.getlist('marriagetype')
                gender = request.form.get('gender')
                nationality = request.form.get('nationality')
                color = request.form.get('color')
                martialstatus = request.form.getlist('martialstatus')
                # qabila = request.form.get('qabila')
                # area = request.form.get('area')
                # city = request.form.get('city')
                
                cursor = db.connection.cursor()
                query = f"""SELECT * FROM man WHERE 
                    gender='{gender}' 
                    and smokingstatus={smokingstatus} 
                    {"and marriagetype in ('" + "','".join(marriagetype)+ "')" if marriagetype else ""}
                    and age between {ageMin} and {ageMax} 
                    and length between {lengthMin} and {lengthMax} 
                    and weight between {weightMin} and {weightMax}
                    and nationality like '%{nationality}%'
                    and color like '%{color}%' 
                    {"and martialstatus in ('" + "','".join(martialstatus)+ "')" if martialstatus else ""}"""
                    # qabila like '%{qabila}%' and
                    # area like '%{area}%' and
                    # city like '%{city}%'
                print(query)
                cursor.execute(query)
                searchResults = cursor.fetchall()
                
                return render_template('home.html', fullname=session.get('fullname'),searchResults=searchResults, data=request.form)

            #In case of Request button pressed
            elif "Request" in request.form:
                requesterid = request.form["requesterid"]
                targetid = request.form["targetid"]
                cursor = db.connection.cursor()
                query = f"SELECT * from request WHERE idrequester={requesterid} and idtarget={targetid}"
                print(query)
                cursor.execute(query)
                result = cursor.fetchone()
                #If this request is already exists
                if result:
                    flash("تم إرسال هذا الطلب من قبل")
                    return render_template('home.html', fullname=session.get('fullname'), data=None)
                #Else insert a new request
                else:
                    cursor.execute(
                        f"""INSERT into request (idrequester,idtarget,requestdate,status) 
                        VALUES ({requesterid}, {targetid}, '{datetime.now()}','جديد')""")
                    db.connection.commit()
                    flash("تم تسجيل طلبكم بنجاح")
                    return render_template('home.html', fullname=session.get('fullname'), data=None)

        else:
            #Check if the user has already a profile or not
            cursor = db.connection.cursor()
            cursor.execute(f"Select idman from man where userid = '{session.get('userid')}'")
            result=cursor.fetchone()
            if result:
                # User is loggedin show them the home page
                return render_template('home.html', fullname=session.get('fullname'), data=None)
            else:
                cursor.execute(
                    f"SELECT * FROM user WHERE iduser = '{session.get('userid')}'")
                account = cursor.fetchone()
                flash('لابد من تسجيل بياناتك أولا حتى تستطيع إستخدام البحث')
                # Show the profile page with account info
                return render_template('profile.html', account=account, data=None)

    # User is not loggedin redirect to login page
    return redirect(url_for('login'))




@app.route('/profile', methods=['GET', 'POST'])
def profile():
    # Check if user is loggedin
    if 'loggedin' in session:
        # We need all the account info for the user so we can display it on the profile page
        cursor = db.connection.cursor()
        cursor.execute(
            f"SELECT * FROM user WHERE iduser = '{session['userid']}'")
        account = cursor.fetchone()
        cursor.execute(
            f"SELECT * FROM man WHERE userid = '{session['userid']}'")
        profile = cursor.fetchone()

        if request.method == 'POST':
            
            # If delete profile pressed
            if "Save" in request.form:
                # idman = request.form['idman']
                # created = request.form['created')
                age = request.form.get('age')
                length = request.form.get('length')
                weight = request.form.get('weight')
                nationality = request.form.get('nationality')
                color = request.form.get('color')
                jobstatus = request.form.get('jobstatus')
                smokingstatus = request.form.get('smokingstatus')
                qabila = request.form.get('qabila')
                martialstatus = request.form.get('martialstatus')
                area = request.form.get('area')
                city = request.form.get('city')
                origin = request.form.get('origin')
                qualifications = request.form.get('qualifications')
                marriagetype = request.form.getlist('marriagetype')
                anothernationality = request.form.get('anothernationality')
                about = request.form.get('about')
                requirments = request.form.get('requirments')
                # userid = request.form.get('userid')
                gender = request.form.get('gender')
                
                # Check if user has already profile, so update, else insert
                if profile:
                    query=f"""
                                UPDATE man
                                    SET
                                    created = '{datetime.now()}',
                                    nationality = '{nationality}',
                                    age = {age},
                                    length = {length},
                                    weight = {weight},
                                    color = '{color}',
                                    jobstatus = '{jobstatus}',
                                    qabila = '{qabila}',
                                    smokingstatus = {smokingstatus},
                                    martialstatus = '{martialstatus}',
                                    origin = '{origin}',
                                    area = '{area}',
                                    city = '{city}',                                    
                                    qualifications = '{qualifications}',
                                    {"marriagetype = '" + (",".join(marriagetype)+ "'," if marriagetype else "علني',")}
                                    anothernationality = {anothernationality},
                                    about = '{about}',
                                    requirments = '{requirments}',
                                    gender = '{gender}'
                                    WHERE userid = '{session['userid']}';"""
                    print(query)
                    cursor.execute(query)
                    db.connection.commit()
                    flash("تم تحديث الملف بنجاح")
                    return render_template('home.html', fullname=session['fullname'],  data=None)

                # Insert instead of update
                else:
                    cursor.execute(f"""
                                INSERT INTO man
                                    (created,
                                    nationality,
                                    age,
                                    length,
                                    weight,
                                    color,
                                    jobstatus,
                                    qabila,
                                    smokingstatus,
                                    martialstatus,
                                    origin,
                                    area,
                                    city,
                                    qualifications,
                                    marriagetype,
                                    anothernationality,
                                    about,
                                    requirments,
                                    userid,
                                    gender)
                                    VALUES
                                    ('{datetime.now()}',
                                    '{nationality}',
                                    '{age}',
                                    '{length}',
                                    '{weight}',
                                    '{color}',
                                    '{jobstatus}',
                                    '{qabila}',
                                    '{smokingstatus}',
                                    '{martialstatus}',
                                    '{origin}',
                                    '{area}',
                                    '{city}',
                                    '{qualifications}',
                                    '{marriagetype}',
                                    '{anothernationality}',
                                    '{about}',
                                    '{requirments}',
                                    '{session['userid']}',
                                    '{gender}');""")
                    db.connection.commit()
                    flash("تم تحديث الملف بنجاح")
                    return render_template('home.html', fullname=session['fullname'], data=None)
                
            #If delete profile pressed    
            elif "Delete" in request.form:
                cursor.execute(f"""Delete from man where userid={session['userid']}""")
                db.connection.commit()
                flash("تم حذف الملف")
                return render_template('home.html', fullname=session['fullname'], data=None)

        else:
            # Show the profile page with account info
            return render_template('profile.html', account=account, data=profile)
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))




@app.route('/requests', methods=['GET', 'POST'])
def requests():
    # Check if user is loggedin
    if 'loggedin' in session and session['fullname']=='Administrator':
        cursor = db.connection.cursor()
        cursor.execute(f"SELECT * FROM request")
        reqs = cursor.fetchall()
        alldata=[]
        for req in reqs:
            data = {}
            requesterid = req['idrequester']
            targetid=req['idtarget']
            cursor.execute(f"SELECT * FROM user WHERE iduser={requesterid}")
            user1data=cursor.fetchone()
            cursor.execute(f"SELECT * FROM user WHERE iduser={targetid}")
            user2data = cursor.fetchone()
            data['matchid'] = req['idmatch']
            data['idman1']=requesterid
            data['fullname1'] = user1data['fullname']
            data['phoneno1'] = user1data['phoneno']
            data['idman2'] = targetid
            data['fullname2'] = user2data['fullname']
            data['phoneno2'] = user2data['phoneno']
            data['status'] = req['status']
            alldata.append(data)
        if request.method == 'POST':
            requesterphoneno = request.form['requesterphoneno']
            targetphoneno = request.form['targetphoneno']
            matchid=request.form['matchid']
            if 'SendConfirmation' in request.form and requesterphoneno:
                status = WhatsApp().Send(requesterphoneno,
                                         f"تم تأكيد طلبكم و سيتم التواصل معكم قريبا للتنسيق")
                msg = 'تم إرسال التأكيد' if 'success' in status else 'فشل في الإرسال'
                cursor.execute(f"UPDATE request SET status = '{msg}' WHERE idmatch = {matchid}")
                db.connection.commit()
                flash(msg)
                return redirect(url_for('requests'))
            elif 'SendRequest' in request.form and targetphoneno:
                query=f"""SELECT    nationality,
                                    age,
                                    length,
                                    weight,
                                    color,
                                    jobstatus,
                                    qabila,
                                    smokingstatus,
                                    martialstatus,
                                    origin,
                                    area,
                                    city,
                                    qualifications,
                                    gender
                        From man
                        Where userid={requesterid}
                """
                cursor.execute(query)
                user1info=cursor.fetchone()
                age = user1info.get('age')
                length = user1info.get('length')
                weight = user1info.get('weight')
                nationality = user1info.get('nationality')
                color = user1info.get('color')
                jobstatus = user1info.get('jobstatus')
                smokingstatus = user1info.get('smokingstatus')
                qabila = user1info.get('qabila')
                martialstatus = user1info.get('martialstatus')
                area = user1info.get('area')
                city = user1info.get('city')
                origin = user1info.get('origin')
                qualifications = user1info.get('qualifications')
                gender = user1info.get('gender')        
                
                msg = "تم إستلام طلب للتواصل معكم برجاء التأكيد"+"\n"+\
                f"""
                الجنس: {gender}
                السن : {age}
                الطول: {length}
                الوزن: {weight}
                الجنسية: {nationality}
                لون البشرة : {color}
                الوظيفة : {jobstatus}
                التدخين : {smokingstatus}
                الحالة الإجتماعية : {martialstatus}
                المؤهل الدراسي : {qualifications}
                المدينة : {city}
                المنطقة : {area}
                القبيلة : {qabila}
                منطقة الأصل : {origin}
                """
                
                print(msg)
                status = WhatsApp().Send(targetphoneno,msg)
                msg = 'تم إرسال الطلب' if 'success' in status else 'فشل في الإرسال'
                cursor.execute(
                    f"UPDATE request SET status = '{msg}' WHERE idmatch = {matchid}")
                db.connection.commit()
                flash(msg)
                return redirect(url_for('requests'))
                # {"status": "success", "message": "Message queued successfully.","message_id": "14623481674784445"}
            elif 'DeleteRequest' in request.form:
                cursor.execute(f"DELETE FROM request WHERE idmatch = {matchid}")
                db.connection.commit()
                flash('تم الحذف بنجاح')
                return redirect(url_for('requests'))
        return render_template('requests.html', requests=alldata)


    # User is not loggedin redirect to login page
    return redirect(url_for('login'))




@app.route('/users', methods=['GET', 'POST'])
def users():
    # Check if user is loggedin
    if 'loggedin' in session and session['fullname'] == 'Administrator':
        cursor = db.connection.cursor()
        cursor.execute(f"SELECT * FROM user")
        users = cursor.fetchall()
        for user in users:
            userid = user['iduser']
            fullname = user['fullname']
            phoneno = user['phoneno']
        if request.method == 'POST':
            
            if 'ResetPassword' in request.form:
                newpassword=forgetpassword(phoneno)
                flash(newpassword)
                return redirect(url_for('users'))
            
            elif 'DeleteUser' in request.form:
                cursor.execute(
                    f"Delete from Request WHERE idrequester = {userid}")
                db.connection.commit()
                cursor.execute(
                    f"Delete from Man WHERE userid = {userid}")
                db.connection.commit()
                cursor.execute(
                    f"Delete from User WHERE iduser = {userid}")
                db.connection.commit()
                flash('تم حذف المشترك')
                return redirect(url_for('users'))

        return render_template('users.html', users=users)

    # User is not loggedin redirect to login page
    return redirect(url_for('login'))




@app.route('/export/<tablename>', methods=['GET'])
def export(tablename):
    si = io.StringIO()
    # cw = csv.writer(si)
    cursor = db.connection.cursor()
    cursor.execute(f'SELECT * FROM {tablename}')
    rows = cursor.fetchall()
    df = pd.DataFrame(rows)
    df.to_csv(si, index=False, encoding='utf-8-sig')

    # cw.writerow([i[0] for i in cursor.description])
    # cw.writerows([r.values() for r in rows])
    response = make_response(si.getvalue())
    response.headers['Content-Disposition'] = 'attachment; filename=report.csv'
    response.headers["Content-type"] = "text/csv"
    return response
    # return "Data exported to arabic_data.csv"

    



@app.route('/forgetpassword/<phoneno>', methods=['GET'])
def forgetpassword(phoneno):
    newclearpassword=''.join(choices(string.ascii_letters+string.digits ,k=8))
    
    updatePassword(phoneno,newclearpassword)

    WhatsApp().Send(phoneno, f'كلمة المرور الجديدة: {newclearpassword}')
    
    flash("تم إرسال كلمة المرور الجديدة")
    # flash(f'Phone no.: {phoneno}\nNew password: {newclearpassword}',category='info')
    # return render_template('index.html')
    return newclearpassword


@app.route('/change-password', methods=['POST'])
def change_password():
    username = session.get('phoneno')
    current_password = request.form['current_password']
    new_password = request.form['new_password']
    confirm_password = request.form['confirm_password']

    # check that the user's current password is correct
    if checkPassword(username, current_password)!=0:
        flash('كلمة السر الحالية غير صحيحة')
        return redirect(url_for('profile'))

    # check that the new password and confirmation match
    if new_password != confirm_password:
        flash('كلمة السر الجديدة غير مطابقة للتأكيد')
        return redirect(url_for('profile'))

    # update the user's password in your database
    updatePassword(username, new_password)
    flash('تم تغيير كلمة السر بنجاح')
    return redirect(url_for('login'))





def create_admin():
    admin_phoneno = '0000000'
    admin_password = generate_password_hash('admin', method="sha256")
    admin_fullname = 'Administrator'
    try:
        cursor = db.connection.cursor()

        # check if admin is already registered
        cursor.execute(f"SELECT * FROM user WHERE phoneno = '{admin_phoneno}'")
        result = cursor.fetchone()
        if result:
            print('Administrator account already exists.')
        else:
            cursor.execute(
                f"INSERT INTO user (fullname, password, phoneno) VALUES('{admin_fullname}', '{admin_password}', '{admin_phoneno}')")
            db.connection.commit()
            code = cursor.lastrowid
            print(
                f'Administrator account created successfully with record id: {code}')
    except Exception as e:
        print(e)


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
    app.run(debug=True,port=5050)

    
