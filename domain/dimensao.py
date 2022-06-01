from config import db


class Dimension(db.Model):
    __tablename__ = 'dimension'
    id_dimension = db.Column(db.Integer, primary_key=True)
    name_dimension = db.Column(db.String)
    attribute = db.relationship('Attribute', backref='dimension')

    def __init__(self, name_dimension):
        self.name_dimension = name_dimension