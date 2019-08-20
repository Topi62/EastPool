from application  import db
from sqlalchemy.sql import text

class Team(db.Model):
   shortname = db.Column(db.String(3), primary_key=True)
   longname = db.Column(db.String(15))

   team = db.relationship("User", backref='account')

   def __init__(self, shortname, longname):
     self.shortname = shortname
     self.longname = longname

   @staticmethod
   def check_teams(home, visit):
      stmt = text("SELECT count(shortname) FROM team WHERE shortname IN (:home, :visit)")
      res = db.engine.execute(stmt, home=home, visit=visit)
      if res == 2:
         return True
      return False  

   
   @staticmethod
   def serie_tables(seasonid):
     stmt = text("SELECT t.longname,"
		 " sum(CASE WHEN (homegamenumwins > 4 AND hometeamid == t.shortname) THEN 1 ELSE 0 END) + sum(CASE WHEN (visitgamenumwins > 4 AND visitorteamid == v.shortname) THEN 1 ELSE 0 END) AS voitot"
		 " FROM match"
		 " JOIN team AS t ON t.shortname = match.hometeamid "
		 " JOIN team AS v ON v.shortname = match.visitorteamid " 
		 " WHERE idseason  == :season"
		 " GROUP BY t.longname").params(season = seasonid)
     res = db.engine.execute(stmt)
     return res 
