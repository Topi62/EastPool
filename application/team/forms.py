from flask_wtf import FlaskForm
from wtforms import StringField, validators

class TeamForm(FlaskForm):
    shortname = StringField("Joukkueen lyhenne", [validators.Length(min=3, max=3)])
    longname = StringField("Joukkueen nimi", [validators.Length(min=3, max=15)])

    class Meta:
        csrf = False
