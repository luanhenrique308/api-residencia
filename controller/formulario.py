from flask import request, jsonify
from config import db
from domain.formulario import Formulario


def createForm():
    data = request.get_json()
    id_atributte = data['id_atributo']
    id_dimension = data['id_dimensao']
    id_question = data['id_question']
    id_tdd = data['id_tdd']
    entry = Formulario(id_dimension, id_atributte, id_question, id_tdd);
    db.session.add(entry)
    db.session.commit()

    return getAllForm()


def getForm():
    data = request.get_json()
    id_form = data['id_form']
    results = db.engine.execute(
        f'''
                SELECT * FROM formulario WHERE id_form = '{id_form}'    
            '''
    )

    return jsonify({"data": [dict(result) for result in results]}), 200


def getAllForm():
    results = db.engine.execute(
        f'''
            SELECT * FROM formulario    
        '''
    )

    return jsonify({"data": [dict(result) for result in results ]}), 200


