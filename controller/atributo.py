import json

from flask import request, jsonify

from config import db
from domain.atributo import Atributo


def createAtributo():
    data = request.get_json()
    id_dimensao = data['id_dimensao']
    nome = data['nome']

    entry = Atributo(nome,id_dimensao)
    db.session.add(entry)
    db.session.commit()

    return getAllAtributos()

def deleteAtributo(id_dimensao = 0):
    data = request.get_json()
    if(id_dimensao != 0):
        db.engine.execute(
            f'''
                    DELETE FROM atributo WHERE id_dimensao = '{data['id_dimensao']}'
                '''
        )
    else:
        db.engine.execute(
            f'''

                            DELETE FROM atributo WHERE id_atributo = '{data['id_atributo']}'    
                        '''
        )
    return getAllAtributos()

def getAtributo():
    data = request.get_json()
    id_atributo =  data['id_atributo']
    results =db.engine.execute(
        f'''
            SELECT * FROM atributo WHERE id_atributo = '{id_atributo}'
        '''
    )

    return jsonify({"data": [dict(result) for result in results]}), 200



def getAllAtributos():
    results = db.engine.execute(
        f'''
                SELECT * FROM atributo    
            '''
    )

    return jsonify({"data": [dict(result) for result in results]}), 200