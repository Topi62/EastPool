from application  import db

class Team(db.Model):
   shortname = db.Column(db.String(3), primary_key=True)
   longname = db.Column(db.String(15))

   account = db.relationship("User", backref='team', lazy=True)
   match = db.relationship("Match", backref='team', lazy=True)
 #  match1 = db.relationship("Match", backref='team', lazy=True)


   def __init__(self, shortname, longname):
     self.shortname = shortname
     self.longname = longname
 
