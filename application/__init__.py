# flask sovellus
from flask import Flask, flash
app = Flask(__name__)

# Tuodaan SQLAlchemy k&auml;ytt&ouml;&ouml;n
from flask_sqlalchemy import SQLAlchemy

import os

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

if os.environ.get("HEROKU"):
    # Herokussa postgresql
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    #paikallisesti sqlite
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///EastPool.db"
    # Pyydet&auml;&auml;n SQLAlchemy&auml; tulostamaan kaikki SQL-kyselyt
    app.config["SQLALCHEMY_ECHO"] = True

# Luodaan db-olio, jota k&auml;ytet&auml;&auml;n tietokannan k&auml;sittelyyn
db = SQLAlchemy(app)


# login functionality
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager, current_user
login_manager = LoginManager()
login_manager.setup_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."


# roles in login_required
from functools import wraps

def login_required(role="ANY"):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user:
                return login_manager.unauthorized()

            if not current_user.is_authenticated:
                return login_manager.unauthorized()
            
            unauthorized = False

            if role != "ANY":
                unauthorized = True
                
                for user_role in current_user.roles():
                     if user_role == role:
                        unauthorized = False
                        break

            if unauthorized:
                return login_manager.unauthorized()
            
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper



# omat toiminnallisuudet
from application import views

from application.auth import models
from application.auth import views

from application.roles import models
from application.roles import views

from application.team import models
from application.team import views

from application.season import models
from application.season import views

from application.match import models
from application.match import views

from application.serietables import views

from application.player import models
from application.player import views
from application.game import models

from application.frame import models

# kirjautuminen

from application.auth.models import User

@login_manager.user_loader
def load_user(user_id):
   return  User.query.get(user_id)

# Luodaan lopulta tarvittavat tietokantataulut

try: 
    db.create_all()
except:
    pass
