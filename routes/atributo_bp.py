from flask import Blueprint

from controller.atributo import createAtributo, getAtributo, getAllAtributos

atributo_bp = Blueprint("atributo_bp", __name__)
atributo_bp.route('/createAtributo', methods=['POST'])(createAtributo)
atributo_bp.route('/getDimension/atributo=<int:id_atributo>', methods=['GET'])(getAtributo)
atributo_bp.route('/getAllAtributo', methods=['GET'])(getAllAtributos)