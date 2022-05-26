from flask import Blueprint

from controller.tdd import createTdd, getAllTdd

tdd_bp = Blueprint('tdd_bp', __name__)
tdd_bp.route('/getAllTdd', methods=['GET'])(getAllTdd)
tdd_bp.route('/createTdd', methods=['POST'])(createTdd)