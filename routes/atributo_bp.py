from flask import Blueprint

from controller.atributo import createAttribute, getAttribute, getAllAttribute, deleteAttribute

attribute_bp = Blueprint("attribute_bp", __name__)
attribute_bp.route('/createAttribute', methods=['POST'])(createAttribute)
attribute_bp.route('/deleteAttribute', methods=['DELETE'])(deleteAttribute)
attribute_bp.route('/getAttribute', methods=['GET'])(getAttribute)
attribute_bp.route('/getAllAttribute', methods=['GET'])(getAllAttribute)