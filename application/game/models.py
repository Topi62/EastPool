from application  import db
from sqlalchemy.sql import text

class Game(db.Model):
   idgame = db.Column(db.Integer, primary_key=True)
   idmatch = db.Column(db.Integer, db.ForeignKey('match.idmatch'))
   homeplayerid = db.Column(db.Integer, db.ForeignKey('player.idplayer'))
   visitorplayerid = db.Column(db.Integer, db.ForeignKey('player.idplayer'))
   starttime = db.Column(db.DateTime)
   endtime = db.Column(db.DateTime)
   homeframewins = db.Column(db.Integer, default = 0)
   visitorframewins = db.Column(db.Integer, default = 0)

   def __init__(self, idmatch, homeplayer, visitorplayer):
     self.idmatch = idmatch
     self.homeplayerid= homeplayer
     self.visitorplayerid = visitorplayer

   def start():
     self.starttime = db.func.current_timestamp()

   def end(vinner, vintype):
     self.endtime = db.func.current_timestamp()
   
   def frame_win(who):
     if who == 1:
         homeframewins = homeframewins + 1
         return
     visitorframewins = visitorframewins + 1

   @staticmethod
   def getGamesOfMatch(idmatch):
      stmt = text("SELECT Game.idgame, Game.idmatch, Game.homeframewins, Game.visitorframewins, h.name AS homePlayerName, v.name AS visitorPlayerName FROM Game "
                "JOIN Player AS  h ON h.idplayer = homeplayerid JOIN player v ON v.idplayer = visitorplayerid "
                "WHERE game.idmatch==:id ORDER BY game.idgame").params(id=idmatch)
      return db.engine.execute(stmt)
