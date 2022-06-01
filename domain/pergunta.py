from config import db


class Question(db.Model):
    __tablename__ = 'question'
    id_question = db.Column(db.Integer, primary_key=True)
    name_question = db.Column(db.String)
    id_attribute = db.Column(db.Integer, db.ForeignKey('attribute.id_attribute'))

    def __init__(self, name_question, id_attribute):
        self.name_question = name_question
        self.id_attribute = id_attribute
