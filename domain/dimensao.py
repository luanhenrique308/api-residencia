from config import db


class Dimensao(db.Model):
    __tablename__ = 'dimensao'
    id_dimensao = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String)
    atributos= db.relationship('Atributo', backref='dimensao')

    def __init__(self, nome):
        self.nome = nome