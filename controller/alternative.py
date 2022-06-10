import json
from flask import request, jsonify
from config import db
from domain.alternatives import Alternative



def createAlternative():
    data = request.get_json()
    id_question = data['id_question']
    name_alternative = data['name_alternative']
    score = data['score']

    entry = Alternative(name_alternative, id_question, score)
    db.session.add(entry)
    db.session.commit()

    return getAllAlternatives()

def getAlternative():
    data = request.get_json()
    id_alternative = data['id_alternative']
    results = db.engine.execute(
        f'''
            SELECT * FROM alternative WHERE id_alternative = '{id_alternative}'    

        '''
    )

    return jsonify({"alternative": [dict(result) for result in results]}), 200

def getAlternativeByQuestion():
    data = request.get_json()
    id_question = data['id_question']
    results = db.engine.execute(
        f'''
                SELECT * FROM alternative WHERE id_question = '{id_question}'    

            '''
    )

    return jsonify({"alternatives": [dict(result) for result in results]}), 200


def getAllAlternatives():
    results = db.engine.execute(
        f'''
                SELECT * FROM alternative    
            '''
    )

    return jsonify({"alternative": [dict(result) for result in results]}), 200