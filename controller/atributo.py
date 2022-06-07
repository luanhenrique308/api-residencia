import json
from flask import request, jsonify, Response
from config import db
from controller.pergunta import deleteQuestion
from domain.atributo import Attribute



def createAttribute():
    data = request.get_json()
    id_dimension = data['id_dimension']
    name_attribute = data['name_attribute']

    entry = Attribute(name_attribute, id_dimension)
    db.session.add(entry)
    db.session.commit()

    return getAllAttribute()

def deleteAttribute(id_dimension = 0):
    data = request.get_json()
    if(id_dimension != 0):
        dbExecute = db.session.query(Attribute.id_attribute).filter(Attribute.id_dimension == id_dimension)
        results = db.session.execute(dbExecute)
        for id_attribute in results:
             deleteQuestion(id_attribute[0])
        db.engine.execute(
            f'''
                    DELETE FROM attribute WHERE id_dimension = '{data['id_dimension']}'
                '''
        )
    else:
        deleteQuestion(data['id_attribute'])
        db.engine.execute(
            f'''

                            DELETE FROM attribute WHERE id_attribute = '{data['id_attribute']}'    
                        '''
        )
    return getAllAttribute()

def getAttribute():
    data = request.get_json()
    id_attribute = data['id_attribute']
    results = db.engine.execute(
        f'''
            SELECT * FROM attribute WHERE id_attribute = '{id_attribute}'    

        '''
    )
    return {
        "user": "John Doe"
    }

def getAllAttribute():
    results = db.engine.execute(
        f'''
                SELECT * FROM attribute    
            '''
    )

    return {
        "user": "John Doe"
    }