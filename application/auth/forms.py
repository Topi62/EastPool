from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
  
class LoginForm(FlaskForm):
    name = StringField("Nimi")
    shortname = StringField("Joukkue")
    password = PasswordField("Salasana")
  
    class Meta:
        csrf = False

class RegUserForm(FlaskForm):
    name = StringField("Nimi")
    shortname = StringField("Joukkue")
    password = PasswordField("Salasana")
    confirm = PasswordField("Toista Salasana")

    class Meta:
        csrf = False

class ChangePw(FlaskForm):
    password = PasswordField("Uusi salasana")
    confirm = PasswordField("Toista salasana")

    class Meta:
        csfr = False

class DelUser(FlaskForm):
    name = StringField("Nimi")
    team = StringField("Joukkue")

    class Meta:
        csfr = False
