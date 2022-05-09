from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:32553964@localhost/residencias'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = '32553964'

db = SQLAlchemy(app)

class Dimensao(db.Model):
    __tablename__ = 'dimensao'

    id_dimensao = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String)
    atributos= db.relationship('Atributo', backref='dimensao', lazy=True)

    def __init__(self, nome):
        self.nome = nome

class Atributo(db.Model):
    __tablename__ = 'atributo'
    id_atributo = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String)
    id_dimensao = db.Column(db.Integer, db.ForeignKey('dimensao.id_dimensao'))
    perguntas= db.relationship('Pergunta', backref='atributo', lazy=True)


    def __init__(self, nome, id_dimensao):
        self.nome = nome
        self.id_dimensao= id_dimensao

class Pergunta(db.Model):
    __tablename__ = 'pergunta'
    id_pergunta = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String)
    id_atributo = db.Column(db.Integer, db.ForeignKey('atributo.id_atributo'))

    def __init__(self, nome, id_atributo):
        self.nome = nome
        self.id_atributo= id_atributo 

@app.route('/dimensao', methods=['POST'])
def addDimensao():
    entry = Dimensao('teste')

    db.session.add(entry)
    db.session.commit()

    return '201'



if __name__ == '__main__':
    db.create_all()
    app.run()