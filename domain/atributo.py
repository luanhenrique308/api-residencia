from config import db


class Atributo(db.Model):
    __tablename__ = 'atributo'
    id_atributo = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String)
    id_dimensao = db.Column(db.Integer, db.ForeignKey('dimensao.id_dimensao'))
    #perguntas= db.relationship('Pergunta', backref='atributo', lazy=True)


    def __init__(self, nome, id_dimensao):
        self.nome = nome
        self.id_dimensao= id_dimensao