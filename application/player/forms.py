from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators

class PlayerForm(FlaskForm):
    name = StringField("Pelinimi", [validators.Length(min=3, max=12, message="Nimen pituus vähintään 3, maksimi 12 merkkiä"), validators.regexp('([ÅÄÖA-Z][åäöa-z -]{,11})+$', message= "Nimessä vain kirjaimia, väliyöntejä tai tavuviiva ja sen tulee alkaa isolla.")])
    member = IntegerField(label="EP Jäsennumero")

    class Meta:
         csrf=False
