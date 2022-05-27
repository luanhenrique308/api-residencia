from flask import Blueprint

from controller.formulario import getAllForm, getForm, createForm

form_bp = Blueprint('form_bp', __name__)
form_bp.route('/createForm', methods=['POST'])(createForm)
form_bp.route('/getForm', methods=['GET'])(getForm)
form_bp.route('/getAllForm', methods=['GET'])(getAllForm)
