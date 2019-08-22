from application  import db
from application.team.models import Team
from sqlalchemy.sql import text
from time import strftime
import datetime

class Match(db.Model):
   idmatch = db.Column(db.Integer, primary_key=True)
   idseason = db.Column(db.Integer, db. ForeignKey('season.idseason'))
   type = db.Column(db.Integer, default=1)
   date = db.Column(db.DateTime)
   hometeamid = db.Column(db.String(3), db.ForeignKey('team.shortname'), nullable=False)
   visitorteamid = db.Column(db.String(3), db.ForeignKey('team.shortname'), nullable=False)
   homegamenumwins = db.Column(db.Integer, default = 0)
   visitgamenumwins = db.Column(db.Integer, default = 0)
   status = db.Column(db.String(1), default='T')

   hometeam = db.relationship("Team", foreign_keys=[hometeamid], uselist=False) 
   visiteam = db.relationship("Team", foreign_keys=[visitorteamid], uselist=False)
   season = db.relationship("Season")
   match = db.relationship("Game")

   def __init__(self, idseason, hometeamid, visitorteamid):
     self.idseason = idseason
     self.hometeamid = hometeamid
     self.visitorteamid = visitorteamid

   @staticmethod
   def create_matches(seasonid):
     teams = Team.query.all()
     for team in teams:
         others = Team.query.filter(Team.shortname != team.shortname).all()
         for other in others:
             match= Match(idseason=seasonid, hometeamid=team.shortname, visitorteamid=other.shortname)
             db.session.add(match)
     db.session.commit()

   @staticmethod
   def get_coming_match():
     today = datetime.datetime.now()
     stmt =text("SELECT strftime('%d.%m. %H:%M', date) AS gamedate, hometeamid, visitorteamid "
                "FROM match WHERE date > :today ORDER BY date ASC").params(today=today)
     matches = db.engine.execute(stmt) 
     return matches
   
   @staticmethod
   def get_played_match():
      stmt =text("SELECT substr(strftime('%d.%m. %H:%M', date),1,6) AS gamedate, hometeamid, visitorteamid, homegamenumwins, visitgamenumwins "
                "FROM match WHERE status IS NOT 'T' ORDER BY date DESC")
      matches = db.engine.execute(stmt) 
      return matches

