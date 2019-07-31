from application  import db

class Team(db.Model):
   idTeam = db.Column(db.Integer, primary_key=True)
   shortName = db.Column(db.String(3))
   longName = db.Column(db.String(15))

   def __init__(self, shorName):
      self.shortName = shortName

   def __init__(self, longName):
      self.longName = longName
