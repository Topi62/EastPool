from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms import StringField, validators

class RoleForm(FlaskForm):
    name = StringField("Nimi", [validators.Length(min=1, max=13)])
    team = StringField("Joukkue", [validators.Length(min=3, max=3)])
    role = SelectField('Role', choices=[('Admin','admin'), ('Captain','captain'), ('Player','player'), ('Visitor','visitor')])

    class Meta:
        csrf = False
