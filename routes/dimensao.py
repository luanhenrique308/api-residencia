from flask import Blueprint

from controller.dimensao import createDimension

dimension_bp = Blueprint('dimensao_bp', __name__)
dimension_bp.route('/createDimension', methods=['POST'])(createDimension)