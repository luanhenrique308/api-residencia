from flask import request

from config import db
from domain.dimensao import Dimensao

def createDimension():
    data = request.get_json()
    nome = data['nome']
    entry = Dimensao(nome)
    db.session.add(entry)
    db.session.commit()
    return {'data':{'nome':nome}}, 201

def removeDimension(id_dimension):
    return id_dimension

def editDimension(id_dimension):
    return  0

def getDimension(id_dimension):
   return  0

def getAllDimension():
    return 0