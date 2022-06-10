from config import db

class Alternative(db.Model):
    __tablename__ = 'alternative'
    id_alternative = db.Column(db.Integer, primary_key=True)
    name_alternative = db.Column(db.String)
    score = db.Column(db.Integer)
    id_question = db.Column(db.Integer, db.ForeignKey('question.id_question'))

    def __init__(self, name_alternative, id_question, score):
        self.name_alternative = name_alternative
        self.id_question = id_question
        self.score = score
