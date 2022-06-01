from flask import request, jsonify
from config import db
from domain.formulario import Form


def createForm():
    data = request.get_json()
    id_attribute = data['id_attribute']
    id_dimension = data['id_dimension']
    id_question = data['id_question']
    id_tdd = data['id_tdd']
    entry = Form(id_dimension, id_attribute, id_question, id_tdd);
    db.session.add(entry)
    db.session.commit()

    return getAllForm()


def getForm():
    data = request.get_json()
    id_form = data['id_form']
    results = db.engine.execute(
        f'''
                SELECT * FROM form WHERE id_form = '{id_form}'    
            '''
    )

    return jsonify({"data": [dict(result) for result in results]}), 200


def getAllForm():
    results = db.engine.execute(
        f'''
            SELECT * FROM form    
        '''
    )

    return jsonify({"forms": [dict(result) for result in results]}), 200


