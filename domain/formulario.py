from config import db

class Form(db.Model):
    __tablename__ = 'form'
    id_form = db.Column(db.Integer, primary_key= True)
    id_dimension = db.Column(db.Integer)
    id_attribute = db.Column(db.Integer)
    id_question = db.Column(db.Integer)
    id_tdd = db.Column(db.Integer, db.ForeignKey('tdd.id_tdd'))

    def __init__(self, id_dimension, id_attribute, id_question, id_tdd):
        # self.nome = nome
        self.id_dimension = id_dimension
        self.id_attribute = id_attribute
        self.id_question = id_question
        self.id_tdd = id_tdd
