from flask import jsonify


def testApi():
    return jsonify({"data":"Hello"})