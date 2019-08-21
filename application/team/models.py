from application  import db
from sqlalchemy.sql import text

class Team(db.Model):
   shortname = db.Column(db.String(3), primary_key=True)
   longname = db.Column(db.String(15))

   team = db.relationship("User", backref='account')
   hometeam= db.relationship("Player", backref='player')

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
     stmt = text("SELECT team.longname,"
		 " (SELECT count(idmatch) FROM match WHERE idseason= :season AND homegamenumwins>4 AND hometeamid = team.shortname) +"
		 " (SELECT count(idmatch) FROM match  WHERE idseason= :season AND visitgamenumwins>4 AND visitorteamid = team.shortname) AS voitot,"
                " (SELECT count(idmatch) FROM match WHERE idseason= :season AND visitgamenumwins>4 AND hometeamid = team.shortname) +"
		 " (SELECT count(idmatch) FROM match  WHERE idseason= :season AND homegamenumwins>4 AND visitorteamid = team.shortname) AS tappiot, "
		
		 " (SELECT COALESCE(sum(homegamenumwins),0) FROM match WHERE idseason= :season AND hometeamid = team.shortname) +"
		 " (SELECT COALESCE(sum(visitgamenumwins), 0) FROM match  WHERE idseason= :season AND visitorteamid = team.shortname) AS pelivoitot, "
		 " (SELECT COALESCE(sum(visitgamenumwins),0) FROM match WHERE idseason= :season AND hometeamid = team.shortname) +"
		 " (SELECT COALESCE(sum(homegamenumwins),0) FROM match  WHERE idseason= :season AND visitorteamid = team.shortname) AS pelitappiot,"     

		 " (SELECT COALESCE(sum(homeframewins),0) FROM game JOIN match ON game.idmatch = match.idmatch WHERE idseason= :season AND hometeamid = team.shortname ) +"
		 " (SELECT COALESCE(sum(visitorframewins), 0) FROM game JOIN match ON game.idmatch = match.idmatch WHERE idseason= :season AND visitorteamid = team.shortname  ) AS erävoitot, "
		 " (SELECT COALESCE(sum(visitorframewins),0) FROM game JOIN match ON game.idmatch = match.idmatch WHERE idseason= :season AND hometeamid = team.shortname  ) +"
		 " (SELECT COALESCE(sum(homeframewins),0) FROM game JOIN match ON game.idmatch = match.idmatch WHERE idseason= :season AND visitorteamid = team.shortname ) AS erätappiot"     
		 " FROM team "
	         " GROUP BY team.shortname, team.longname ORDER BY voitot DESC, pelivoitot  DESC, erävoitot  DESC ").params(season = seasonid)	 
		
     res = db.engine.execute(stmt)
     return res 
