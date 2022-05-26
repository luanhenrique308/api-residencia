from flask import Blueprint

from controller.pergunta import getAllQuestion, getQuestion, deleteQuestion, createQuestion

question_bp = Blueprint('question_bp', __name__)
question_bp.route('/createQuestion', methods=['POST'])(createQuestion)
question_bp.route('/deleteQuestion', methods=['DELETE'])(deleteQuestion)
question_bp.route('/getQuestion', methods=['GET'])(getQuestion)
question_bp.route('/getAllQuestion', methods=['GET'])(getAllQuestion)