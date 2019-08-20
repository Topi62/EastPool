from application  import db

class Player(db.Model):
   idplayer = db.Column(db.Integer, primary_key=True)
   idteam = db.Column(db.String(3), db. ForeignKey('team.shortname'), nullable=False)
   name = db.Column(db.String(12), nullable=False)
   nromember = db.Column(db.Integer)


   def __init__(self, idteam, name, nromember):
     self.idteam = idteam
     self.name = name
     self.nromember = nromember

