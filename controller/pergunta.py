import json
from flask import request, jsonify
from config import db
from domain.pergunta import Pergunta


def createQuestion():
    data = request.get_json()
    id_atributo = data['id_atributo']
    nome = data['nome']

    entry = Pergunta(nome,id_atributo)
    db.session.add(entry)
    db.session.commit()

    return getAllQuestion()

def deleteQuestion(id_atributo = 0):
    # print(id_atributo)
    data = request.get_json()
    if(id_atributo != 0):
        db.engine.execute(
            f'''
                    DELETE FROM pergunta WHERE id_atributo = '{id_atributo}'    
                '''
        )
    else:
        db.engine.execute(
                f'''
                    DELETE FROM pergunta WHERE id_pergunta = '{data['id_question']}'    
                '''
            )
    return getAllQuestion()

def getQuestion():
    data = request.get_json()
    id_question =  data['id_question']
    results =db.engine.execute(
        f'''
            SELECT * FROM pergunta WHERE id_pergunta = '{id_question}'
        '''
    )

    return jsonify({"data": [dict(result) for result in results]}), 200



def getAllQuestion():
    results = db.engine.execute(
        f'''
                SELECT * FROM pergunta    
            '''
    )

    return jsonify({"data": [dict(result) for result in results]}), 200