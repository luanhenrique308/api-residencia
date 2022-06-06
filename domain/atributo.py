from config import db

class Attribute(db.Model):
    __tablename__ = 'attribute'
    question = db.relationship('Question', backref='attribute')
    id_attribute = db.Column(db.Integer, primary_key=True)
    name_attribute = db.Column(db.String)
    id_dimension = db.Column(db.Integer, db.ForeignKey('dimension.id_dimension', ondelete='CASCADE'))

    def __init__(self, name_attribute, id_dimension):
        self.name_attribute = name_attribute
        self.id_dimension= id_dimension
