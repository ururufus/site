from ..extensions import db

class PostForm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    attendance = db.Column(db.String(10))  # 'yes' или 'no'
    alcohol = db.Column(db.Text)           # 'white_wine,red_wine'
    song = db.Column(db.String(200))
    diet = db.Column(db.Text)
    submitted_at = db.Column(db.DateTime, default=db.func.now())
