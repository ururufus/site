from ..extensions import db

class PostMenu(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(1000))
