from application import db
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import text

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    name = db.Column(db.String(14), nullable=False)
    team = db.Column(db.String(3), ForeignKey('team.shortname'), nullable=False)
    role = db.Column(db.String(7), nullable=False)

    def __init__(self, name, team, role):
        self.name = name
        self.team = team
        self.role = role

    @staticmethod
    def getRoles(name, team):
       stmt = text("SELECT role FROM role WHERE name= :name AND team = :team").params(name=name, team=team)
       res = db.engine.execute(stmt)
       return list(res)
