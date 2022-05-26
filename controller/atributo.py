from flask import request

from config import db
from domain.atributo import Atributo


def createAtributo():
    data = request.get_json()
    id_dimensao = data['id_dimensao']
    nome = data['nome']

    entry = Atributo(nome,id_dimensao)
    db.session.add(entry)
    db.session.commit()

    return "201"

def deleteAtributo(id_dimensao = 0):
    data = request.get_json()
    # id_atributo = data['id_atributo']
    # print(args.get('id_dimensao'))
    #
    if(id_dimensao != 0):
        results = db.engine.execute(
            f'''
                    DELETE FROM atributo WHERE id_dimensao = '{data['id_dimensao']}'
                '''
        )
    else:
        results = db.engine.execute(
            f'''

                            DELETE FROM atributo WHERE id_atributo = '{data['id_atributo']}'    
                        '''
        )
    return '200'

def getAtributo(id_atributo):
    return '0'

def getAllAtributos():
    results = db.engine.execute(
        f'''
                SELECT * FROM atributo    
            '''
    )

    return '200'