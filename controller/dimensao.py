from flask import request, jsonify

from config import db
from domain.dimensao import Dimensao


def createDimension():
    data = request.get_json()
    nome = data['nome']
    entry = Dimensao(nome)
    db.session.add(entry)
    db.session.commit()

    dimensionAll = Dimensao.query.all()

    def d():
        for val in dimensionAll:
            return val.nome

    return '201'


def deleteDimension():
    args = request.args
    print(args.get('id_dimension'))
    results = db.engine.execute(
        f'''
            DELETE FROM dimensao WHERE id_dimensao = '{args.get('id_dimension')}'    
        '''
        )
    return '200'


def editDimension(id_dimension):
    return 0


def getDimension(id_dimension):
    return 0


def getAllDimension():
    return 0
