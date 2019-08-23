from application import db
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from application.roles.models import Role

class User(db.Model):

    __tablename__ = 'account'

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    name = db.Column(db.String(14), nullable=False)
    team = db.Column(db.String(3), ForeignKey('team.shortname'), nullable=False)
    username = db.Column(db.String(18), nullable=True)
    password = db.Column(db.String(8), nullable=False)

    def __init__(self, name, shortname, password):
        self.name = name
        self.team = shortname
        self.password = password
        self.username = name + " " + shortname

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def roles(self):
        roles =  Role.getRoles(self.name, self.team)
        if not roles:
             return  []
        return roles
