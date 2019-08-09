from application  import db

class Match(db.Model):
   idmatch = db.Column(db.Integer, primary_key=True)
   idseason = db.Column(db.Integer, db. ForeignKey('season.idseason'))
   type = db.Column(db.Integer, default=1)
   date = db.Column(db.DateTime)
   hometeamid = db.Column(db.String(3), db.ForeignKey('team.shortname'), nullable=False)
   visitorteamid = db.Column(db.String(3), db.ForeignKey('team.shortname'), nullable=False)
   homegamenumwins = db.Column(db.Integer, default = 0)
   visitgamenumwins = db.Column(db.Integer, default = 0)
   status = db.Column(db.String(1), default='T')

   hometeam = db.relationship("Team", foreign_keys=[hometeamid], uselist=False) 
   visiteam = db.relationship("Team", foreign_keys=[visitorteamid], uselist=False)
   season = db.relationship("Season")

   def __init__(self, idseason, hometeamid, visitorteamid):
     self.idseason = idseason
     self.hometeamid = hometeamid
     self.visitorteamid = visitorteamid
