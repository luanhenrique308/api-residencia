from flask import request

from config import db
from domain.atributo import Atributo


def createAtributo():
    data = request.get_json()
    id_dimensao = data['id_dimensao']
    nome = data['nome']

    entry = Atributo('luan',1)
    db.session.add(entry)
    db.session.commit()

    return {'data':{'nome':nome}}, 201

def getAtributo(id_atributo):
    return 0

def getAllAtributos():
    return 0