from datetime import date

from flask import request, jsonify
from config import db
from domain.tdd import Tdd


def createTdd():
    data = request.get_json()
    client = data['client']
    creation_date = data['creation_date']

    entry = Tdd(client, creation_date)
    db.session.add(entry)
    db.session.commit()
    return getAllTdd()

def getAllTdd():
    results = db.engine.execute(
        f'''
                    SELECT * FROM tdd    
                '''
    )
    return jsonify({"data": [dict(result) for result in results]}), 200
