from app import db

class Files(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    filename = db.Column(db.String(300))
    data = db.Column(db.LargeBinary)
