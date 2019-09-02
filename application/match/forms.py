from application import db
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DateField, HiddenField, validators
from wtforms.fields.html5 import DateTimeLocalField
from datetime import datetime, timedelta
from sqlalchemy import or_

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


class SelectPlayersForm(FlaskForm):
    home1 = SelectField('Kotipelaaja',coerce=int)
    home2 = SelectField('Kotipelaaja', coerce=int)
    home3 = SelectField('Kotipelaaja', coerce=int)
    visit1 = SelectField('Vieraspelaaja', coerce=int)
    visit2 = SelectField('Vieraspelaaja', coerce=int)
    visit3 = SelectField('Vieraspelaaja',coerce=int)
    match = HiddenField("Ottelu")

    class Meta:
        csrf = False


class SelectMatchForm(FlaskForm):
    match= SelectField('Ottelu', coerce=int)

    class Meta:
        csrf = False



