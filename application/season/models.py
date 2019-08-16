from application  import db

class Season(db.Model):
   idseason = db.Column(db.Integer, primary_key=True)
   period = db.Column(db.String(9))

   def __init__(self, id,  period):
     self.idseason = id
     self.period = period

