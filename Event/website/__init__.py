from mimetypes import init
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from werkzeug.security import generate_password_hash, check_password_hash


db=SQLAlchemy()
db_name="database.db"

def create_app():
    from .models import User, Note
    from .views import views
    from .auth import auth

    app=Flask(__name__)
    app.config['SECRET_KEY']="1234567"
    app.config['SQLALCHEMY_DATABASE_URI']=f"sqlite:///{db_name}"
    db.init_app(app)
            
    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app



def create_database(app):
    if not path.exists(f"website/{db_name}"):
        with app.app_context():
            db.create_all()
        print("Database created successfully")
    print(create_admin(app))



def create_admin(app):
    from .models import User, Note

    try:
        admin_email = 'admin@here.com'
        admin_password = generate_password_hash('admin', method="sha256")
        admin_fullname = 'Administrator'

        with app.app_context():
            #if admin exists, reset password else create
            if user := User.query.filter_by(email=admin_email).first():
                user.password = admin_password
                user.fullname = admin_fullname
            else:
                new_user = User(email=admin_email, password=admin_password, fullname=admin_fullname)
                db.session.add(new_user)
            db.session.commit()
        return 'Administrator account created successfully'
    except Exception as e:
        return e

