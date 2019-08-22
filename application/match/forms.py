from application import db
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, validators
from wtforms.fields.html5 import DateTimeLocalField

class NewMatchForm(FlaskForm):
    season = StringField("Kausi", [validators.regexp('[0-9]+', 0, "Kaudet numeroitu")])
    hometeam = StringField("Kotijoukkue", [validators.regexp('[ÅÄÖA-Z][ÅÄÖA-Z][0-9]', 0, "Tunnuksessa on kaksi isoa kirjainta ja numero")])
    visitteam = StringField("Vierasjoukkue", [validators.regexp('[ÅÄÖA-Z]{2}[0-9]', 0, "Tunnuksessa on kaksi isoa kirjainta ja numero")])

    class Meta:
        csrf = False

class TimeMatchForm(FlaskForm):
    season = StringField("Kausi", [validators.regexp('[0-9]+', 0, "Kaudet numeroitu")])
    gamedate = DateTimeLocalField(label="Pelipäivä ja aika", format='%Y-%m-%dT%H:%M', validators=[validators.InputRequired()])
    hometeam = StringField("Kotijoukkue", [validators.regexp('[ÅÄÖA-Z][ÅÄÖA-Z][0-9]', 0, "Tunnuksessa on kaksi isoa kirjainta ja numero")])
    visitteam = StringField("Vierasjoukkue", [validators.regexp('[ÅÄÖA-Z]{2}[0-9]', 0, "Tunnuksessa on kaksi isoa kirjainta ja numero")])

    class Meta:
        csrf = False

class ListMatchForm(FlaskForm):
    season = StringField("Kausi")
    hometeam = StringField("Koti")
    visitteam = StringField("Vieras")
    gamedate = DateTimeLocalField("Pelipäivä", format='%Y-%m-%dT%H:%M')
    tulos = StringField("Pelit")
    erat = StringField("Erät")

    class Meta:
        csrf = False
