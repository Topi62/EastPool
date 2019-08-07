from application  import db

class Team(db.Model):
   idteam = db.Column(db.Integer, primary_key=True)
   shortname = db.Column(db.String(3))
   longname = db.Column(db.String(15))

   def __init__(self, shortname, longname):
     self.shortname = shortname
     self.longname = longname
 
