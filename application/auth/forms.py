from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
from wtforms import StringField, validators

  
class LoginForm(FlaskForm):
    name = StringField("Nimi", [validators.Length(min=1, max=13)])
    shortname = StringField("Joukkue", [validators.Length(min=3, max=3)])
    password = PasswordField("Salasana", [validators.Length(min=1, max=8)])
  
    class Meta:
        csrf = False

class RegUserForm(FlaskForm):
    name = StringField("Nimi")
    shortname = StringField("Joukkue", [validators.Length(min=3, max=3)])
    password = PasswordField("Salasana", [validators.Length(min=1, max=8)])
    confirm = PasswordField("Toista Salasana", [validators.Length(min=1, max=8)])

    class Meta:
        csrf = False

class ChangePw(FlaskForm):
    password = PasswordField("Uusi salasana", [validators.Length(min=1, max=8)])
    confirm = PasswordField("Toista salasana", [validators.Length(min=1, max=8)])

    class Meta:
        csfr = False

class DelUser(FlaskForm):
    name = StringField("Nimi", [validators.Length(min=1, max=14)])
    team = StringField("Joukkue", [validators.Length(min=3, max=3)])

    class Meta:
        csfr = False
