from config import db

class Formulario(db.Model):
    __tablename__ = 'formulario'
    id_form = db.Column(db.Integer, primary_key= True)
    id_dimension = db.Column(db.Integer)
    id_atributte = db.Column(db.Integer)
    id_question = db.Column(db.Integer)
    id_tdd = db.Column(db.Integer, db.ForeignKey('tdd.id_tdd'))

    def __init__(self, id_dimensao, id_atributo, id_question, id_tdd):
        # self.nome = nome
        self.id_dimensao = id_dimensao
        self.id_atributo= id_atributo
        self.id_question = id_question
        self.id_tdd = id_tdd
