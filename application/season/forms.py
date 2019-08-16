from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, validators

class SeasonForm(FlaskForm):
    seasonid = IntegerField("Kauden id", [validators.NumberRange(1,99,"Kokonaislukuna")])
    period = StringField("Kauden nimi", [validators.Length(min=1, max=9)])
    games = BooleanField("Luodaanko ottelut?")

    class Meta:
        csrf = False
