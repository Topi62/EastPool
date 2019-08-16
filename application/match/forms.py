from application import db
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, validators

class NewMatchForm(FlaskForm):
    season = StringField("Kausi", [validators.regexp('[0-9]+', 0, "Kaudet numeroitu")])
    hometeam = StringField("Kotijoukkue", [validators.regexp('[ÅÄÖA-Z][ÅÄÖA-Z][0-9]', 0, "Tunnuksessa on kaksi isoa kirjainta ja numero")])
    visitteam = StringField("Vierasjoukkue", [validators.regexp('[ÅÄÖA-Z]{2}[0-9]', 0, "Tunnuksessa on kaksi isoa kirjainta ja numero")])

    class Meta:
        csrf = False

class TimeMatchForm(FlaskForm):
    season = StringField("Kausi", [validators.regexp('[0-9]+', 0, "Kaudet numeroitu")])
    gamedate = DateField(label="Pelipäivä ja aika", validators=[validators.InputRequired("Anna pelipäivä ja kelloaika")])
    hometeam = StringField("Kotijoukkue", [validators.regexp('[ÅÄÖA-Z][ÅÄÖA-Z][0-9]', 0, "Tunnuksessa on kaksi isoa kirjainta ja numero")])
    visitteam = StringField("Vierasjoukkue", [validators.regexp('[ÅÄÖA-Z]{2}[0-9]', 0, "Tunnuksessa on kaksi isoa kirjainta ja numero")])

    class Meta:
        csrf = False

class ListMatchForm(FlaskForm):
    season = StringField("Kausi")
    hometeam = StringField("Koti")
    visitteam = StringField("Vieras")
    gamedate = DateField("Pelipäivä")
    tulos = StringField("Pelit")
    erat = StringField("Erät")

    class Meta:
        csrf = False
