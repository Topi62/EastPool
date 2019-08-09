from application  import db

class Team(db.Model):
   shortname = db.Column(db.String(3), primary_key=True)
   longname = db.Column(db.String(15))

   team = db.relationship("User", backref='account')

   def __init__(self, shortname, longname):
     self.shortname = shortname
     self.longname = longname
 
