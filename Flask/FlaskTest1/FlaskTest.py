from flask import Flask,render_template,request,flash
from flask_mysqldb import MySQL
from random import choice
from flask_bootstrap import Bootstrap 

app = Flask(__name__)
app.config["SECRET_KEY"] ="12qwaszx#E"

# Required
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "P@ssw0rd1234567"
app.config["MYSQL_DB"] = "eventregistration"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"
db = MySQL(app)

#Create bootstrap
Bootstrap(app)

@app.route('/register', methods=['GET', 'POST'])
def register():
    data={}
    if request.method == "POST":
        data = request.form
        phoneno = data.get('PhoneNo')
        firstname = data.get('FirstName')
        parentname = data.get('ParentName')
        firstgrandname = data.get('FirstGrandName')
        secondgrandname = data.get('SecondGrandName')
        thirdgrandname = data.get('ThirdGrandName')
        familyid = data.get('FamilyId')
        genderid = data.get('GenderId')
        agerangeid = data.get('AgeRangeId')
        email = data.get('Email')
        city = data.get('CityName')
        willattend = data.get('WillYouAttend')
        relation = data.get('RelationToFamily')
        ideas = data.get('Ideas')
        
        if phoneno:
            cur = db.connection.cursor()
            cur.execute(
                f'''SELECT idGuest FROM guests where phoneno = {phoneno}''')
            result = cur.fetchall()
            # cur.close()
            if result:
                return render_template('register.html', msg=" رقم الجوال مسجل من قبل",data=data)
            else:
                try:
                    cur.execute(f'''INSERT INTO guests
                        (FamilyId,
                        FirstName,
                        ParentName,
                        FirstGrandName,
                        SecondGrandName,
                        ThirdGrandName,
                        RelationToFamily,
                        AgeRangeId,
                        GenderId,
                        PhoneNo,
                        CityName,
                        WillYouAttend,
                        Ideas,
                        Email)
                        VALUES
                        ({familyid},
                        '{firstname}',
                        '{parentname}',
                        '{firstgrandname}',
                        '{secondgrandname}',
                        '{thirdgrandname}',
                        '{relation}',
                        {agerangeid},
                        {genderid},
                        '{phoneno}',
                        '{city}',
                        {willattend},
                        '{ideas}',
                        '{email}');
                        ''')
                    db.connection.commit()
                    code = cur.lastrowid
                    return render_template('code.html', type='exist', code=code)
                except Exception as e:
                    return render_template('register.html',msg=e, data=data)

    return render_template('register.html', data=data)


@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        # phoneno = request.form.get('PhoneNo')
        data = request.form
        phoneno = data.get('PhoneNo')

        cur = db.connection.cursor()
        cur.execute(f'''SELECT idGuest FROM guests where phoneno = {phoneno}''')
        result = cur.fetchall()      
        if not result:
            return render_template('login.html',msg="رقم الجوال غير مسجل")
        else:
            # ({'idGuest': 35},)
            code = result[0].get('idGuest')
            return render_template('code.html', type='exist', code=code)


    return render_template('login.html')


@app.get('/code/<phoneno>')
def code(phoneno):
    cur = db.connection.cursor()
    cur.execute(f'''SELECT idGuest FROM guests where phoneno = {phoneno}''')
    result = cur.fetchall()
    if result:      
        code = result[0].get('idGuest')
        return render_template('code.html',type='exist',code=code)
    else:
        return render_template('code.html',type="not exist")


@app.route('/confirm', methods=['GET', 'POST'])
def confirm():
    if request.method == "POST":
        data = request.form
        phoneno = data.get('PhoneNo')

        cur = db.connection.cursor()
        cur.execute(
            f'''SELECT idGuest FROM guests where phoneno = {phoneno}''')
        result = cur.fetchall()
        if not result:
            return render_template('confirm.html', msg="رقم الجوال غير مسجل")
        else:
            cur = db.connection.cursor()
            cur.execute(
            f'''UPDATE guests set confirmed=1 where phoneno = {phoneno}''')
            db.connection.commit()
            # ({'idGuest': 35},)
            code = result[0].get('idGuest')
            return render_template('code.html', type='confirm', code=code)

    return render_template('confirm.html')


@app.route('/withdraw', methods=['GET'])
def withdraw():
    cur = db.connection.cursor()
    cur.execute(
        f'''SELECT idGuest, CONCAT(firstname," ",parentname," ",firstgrandname," ",secondgrandname," ",thirdgrandname) as fullname FROM guests where confirmed=1''')
    result = cur.fetchall()
    if not result:
        return render_template('withdraw.html', msg="لا يوجد ضيوف أكدوا الحضور")
    else:
        guests=[t.get('idGuest') for t in result]
        winnerid = choice(guests)
        winnercode=str(winnerid).zfill(3)
        winnername=list(filter(lambda x:x.get('idGuest')==winnerid,result))[0].get('fullname')
        return render_template('withdraw.html', winnerid=winnercode,winnername=winnername)


# @app.get('/guests/<phoneno>')
@app.route('/guests', methods=['GET','POST'])
def guests():
    cur = db.connection.cursor()
    cur.execute(f'''SELECT * FROM guests''')
    result = cur.fetchall()
    if result:
        return render_template('guests.html', guests=result)
    else:
        return render_template('guests.html', msg='No guest')


@app.route('/delete_guest/<guestid>', methods=['GET', 'POST'])
def delete_guest(guestid):
    cur = db.connection.cursor()
    cur.execute(f'''DELETE FROM guests where idGuest={guestid}''')
    db.connection.commit()
    print('Deleting guest',guestid)
    return guests()

if __name__ == '__main__':
    app.run(debug=True)
