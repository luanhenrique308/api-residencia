import json
from flask import request, jsonify
from config import db
from domain.pergunta import Question


def createQuestion():
    data = request.get_json()
    id_attribute = data['id_attribute']
    question = data['question']

    entry = Question(question, id_attribute)
    db.session.add(entry)
    db.session.commit()

    return getAllQuestion()

def deleteQuestion(id_attribute = 0):
    data = request.get_json()
    if(id_attribute != 0):
        db.engine.execute(
            f'''
                    DELETE FROM question WHERE id_attribute = '{id_attribute}'    
                '''
        )
    else:
        db.engine.execute(
                f'''
                    DELETE FROM question WHERE id_question = '{data['id_question']}'    
                '''
            )
    return getAllQuestion()

def getQuestion():
    data = request.get_json()
    id_question = data['id_question']
    results = db.engine.execute(
        f'''
            SELECT * FROM question WHERE id_question = '{id_question}'
        '''
    )

    return jsonify({"question": [dict(result) for result in results]}), 200



def getAllQuestion():
    results = db.engine.execute(
        f'''
                SELECT * FROM question    
            '''
    )

    return jsonify({"questions": [dict(result) for result in results]}), 200