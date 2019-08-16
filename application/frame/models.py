from application  import db

class Frame(db.Model):
   idframe = db.Column(db.Integer, primary_key=True)
   idgame = db.Column(db.Integer, db. ForeignKey('game.idgame'))
   starttime = db.Column(db.DateTime)
   endtime = db.Column(db.DateTime)
   vinner = db.Column(db.Integer, default = 0)
   vintype = db.Column(db.Integer, default = 0)

   game = db.relationship("Game")

   def __init__(self, idseason, hometeamid, visitorteamid):
     self.idseason = idseason
     self.hometeamid = hometeamid
     self.visitorteamid = visitorteamid

   def start():
     self.starttime = db.func.current_timestamp()

   def end(vinner, vintype):
     self.endtime = db.func.current_timestamp()
     self.vinner = vinner
     self.vintype = vintype
