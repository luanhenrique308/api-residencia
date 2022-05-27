from config import db

class Tdd(db.Model):
    __tablename__ = 'tdd'
    id_tdd = db.Column(db.Integer, primary_key = True)
    criation_date = db.Column(db.Date)
    client = db.Column(db.String)
    formulario= db.relationship('Formulario', backref='tdd')

    def __init__(self, client, criation_date):
        self.client= client
        self.criation_date= criation_date