from flask import Blueprint

from controller.atributo import createAtributo, getAtributo, getAllAtributos, deleteAtributo

atributo_bp = Blueprint("atributo_bp", __name__)
atributo_bp.route('/createAtributo', methods=['POST'])(createAtributo)
atributo_bp.route('/deleteAttribute', methods=['DELETE'])(deleteAtributo)
atributo_bp.route('/getAttribute', methods=['GET'])(getAtributo)
atributo_bp.route('/getAllAtributo', methods=['GET'])(getAllAtributos)