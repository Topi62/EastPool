# coding=utf-8
from flask import Flask
app = Flask(__name__)

# Tuodaan SQLAlchemy käyttöön
from flask_sqlalchemy import SQLAlchemy

# Käytetään EastPool.db-nimistä SQLite-tietokantaa. Kolme vinoviivaa
# kertoo, tiedosto sijaitsee tämän sovelluksen tiedostojen kanssa
# samassa paikassa
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///EastPool.db"
# Pyydetään SQLAlchemyä tulostamaan kaikki SQL-kyselyt
app.config["SQLALCHEMY_ECHO"] = True

# Luodaan db-olio, jota käytetään tietokannan käsittelyyn
db = SQLAlchemy(app)

from application.schedule import models
from application.team import views

# Luodaan lopulta tarvittavat tietokantataulut
db.create_all()
