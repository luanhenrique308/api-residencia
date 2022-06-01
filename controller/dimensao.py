from flask import request, jsonify

from config import db
from controller.atributo import deleteAttribute
from domain.dimensao import Dimension


def createDimension():
    data = request.get_json()
    name_dimension = data['name_dimension']
    entry = Dimension(name_dimension)
    db.session.add(entry)
    db.session.commit()

    return getAllDimensions()


def deleteDimension():
    data = request.get_json()
    id_dimension = data['id_dimension']
    deleteAttribute(id_dimension)
    results = db.engine.execute(
        f'''
            DELETE FROM dimension WHERE id_dimension = '{id_dimension}'   
        '''
        )
    return getAllDimensions()


def editDimension(id_dimension):
    return 0


def getDimension():
    data = request.get_json()
    id_dimension = data['id_dimension']
    # args = request.args
    results = db.engine.execute(
        f'''
                SELECT * FROM dimension WHERE id_dimension = '{id_dimension}'    
            '''
    )

    return jsonify({"dimension": [dict(result) for result in results]}), 200


def getAllDimensions():
    results = db.engine.execute(
        f'''
            SELECT * FROM dimension    
        '''
    )

    return jsonify({"dimensions": [dict(result) for result in results]}), 200


