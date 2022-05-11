from config import db


class Pergunta(db.Model):
    __tablename__ = 'pergunta'
    id_pergunta = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String)
    id_atributo = db.Column(db.Integer, db.ForeignKey('atributo.id_atributo'))

    def __init__(self, nome, id_atributo):
        self.nome = nome
        self.id_atributo= id_atributo
