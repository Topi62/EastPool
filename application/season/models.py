from application  import db

class Season(db.Model):
   idseason = db.Column(db.Integer, primary_key=True)
   period = db.Column(db.String(8))

   matchs = db.relationship("Match", backref='idseason', lazy=True)

   def __init__(self, period):
     self.period = period

