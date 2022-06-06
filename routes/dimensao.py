from flask import Blueprint

from controller.dimensao import createDimension, deleteDimension, getDimension, getAllDimensions

dimension_bp = Blueprint('dimensao_bp', __name__)
dimension_bp.route('/createDimension', methods=['POST'])(createDimension)
dimension_bp.route('/deleteDimension', methods=['DELETE'])(deleteDimension)
dimension_bp.route('/getDimension', methods=['GET'])(getDimension)
dimension_bp.route('/getAllDimensions', methods=['GET'])(getAllDimensions)
