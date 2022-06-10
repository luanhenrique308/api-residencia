from flask import Blueprint

from controller.alternative import createAlternative, getAllAlternatives, getAlternative, getAlternativeByQuestion

alternative_bp = Blueprint("alternative_bp", __name__)
alternative_bp.route('/createAlternative', methods=['POST'])(createAlternative)
alternative_bp.route('/getAlternative', methods=['GET'])(getAlternative)
alternative_bp.route('/getAllAlternative', methods=['GET'])(getAllAlternatives)
alternative_bp.route('/getAllAlternativeByQuestion', methods=['GET'])(getAlternativeByQuestion)