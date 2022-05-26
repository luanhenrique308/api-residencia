from flask import request, jsonify

from config import db
from controller.atributo import deleteAtributo
from domain.dimensao import Dimensao


def createDimension():
    data = request.get_json()
    nome = data['nome']
    entry = Dimensao(nome)
    db.session.add(entry)
    db.session.commit()

    return getAllDimension()


def deleteDimension():
    data = request.get_json()
    id_dimensao = data['id_dimensao']
    deleteAtributo(id_dimensao)
    results = db.engine.execute(
        f'''
            DELETE FROM dimensao WHERE id_dimensao = '{id_dimensao}'   
        '''
        )
    return getAllDimension()


def editDimension(id_dimension):
    return 0


def getDimension():
    data = request.get_json()
    id = data['id_dimensao']
    # args = request.args
    results = db.engine.execute(
        f'''
                SELECT * FROM dimensao WHERE id_dimensao = '{id}'    
            '''
    )

    return jsonify({"data": [dict(result) for result in results]}), 200


def getAllDimension():
    results = db.engine.execute(
        f'''
            SELECT * FROM dimensao    
        '''
    )

    return jsonify({"data": [dict(result) for result in results ]}), 200


