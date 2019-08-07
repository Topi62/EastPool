from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
  
class LoginForm(FlaskForm):
    name = StringField("Nimi")
    team = StringField("Joukkue")
    password = PasswordField("Salasana")
  
    class Meta:
        csrf = False
