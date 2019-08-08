# flask sovellus
from flask import Flask
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

# omat toiminnallisuudet
from application import views

from application.team import models
from application.team import views

from application.season import models

from application.match import models

from application.auth import models 
from application.auth import views 

# kirjautuminen
from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view =  "auth_login"
login_manager.login_message = "Toiminto vaatii kirjautumisen."

@login_manager.user_loader
def load_user(user_id):
   return  User.query.get(user_id)

# Luodaan lopulta tarvittavat tietokantataulut

try: 
    db.create_all()
except:
    pass
