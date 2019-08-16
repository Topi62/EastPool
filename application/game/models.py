from application  import db

class Game(db.Model):
   idgame = db.Column(db.Integer, primary_key=True)
   idmatch = db.Column(db.Integer, db.ForeignKey('match.matchid'))
   homeplayerid = db.Column(db.Integer, db.ForeignKey('player.idplayer'))
   visitorplayerid = db.Column(db.Integer, db.ForeignKey('player.idplayer'))
   starttime = db.Column(db.DateTime)
   endtime = db.Column(db.DateTime)
   homeframewins = db.Column(db.Integer, default = 0)
   visitorframewins = db.Column(db.Integer, default = 0)

   homeplayer = db.relationship("Team", foreign_keys=['homeplayerid'], uselist=False)
   visitplayer = db.relationship("Team", foreign_keys=['visitorplayerid'], uselist=False) 
   match = db.relationship("Match")

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
