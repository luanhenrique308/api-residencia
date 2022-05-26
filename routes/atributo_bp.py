from flask import Blueprint

from controller.atributo import createAttribute, getAtributo, getAllAtributos, deleteAtributo

atributo_bp = Blueprint("atributo_bp", __name__)
atributo_bp.route('/createAttribute', methods=['POST'])(createAttribute)
atributo_bp.route('/deleteAttribute', methods=['DELETE'])(deleteAtributo)
atributo_bp.route('/getAttribute', methods=['GET'])(getAtributo)
atributo_bp.route('/getAllAtributo', methods=['GET'])(getAllAtributos)