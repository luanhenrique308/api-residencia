from config import db

class Tdd(db.Model):
    __tablename__ = 'tdd'
    id_tdd = db.Column(db.Integer, primary_key = True)
    creation_date = db.Column(db.Date)
    client = db.Column(db.String)
    form= db.relationship('Form', backref='tdd')

    def __init__(self, client, creation_date):
        self.client = client
        self.creation_date = creation_date