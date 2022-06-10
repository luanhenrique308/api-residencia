from flask import Blueprint
from controller.test import testApi

test_bp = Blueprint('test_bp', __name__)
test_bp.route('/', methods=['GET'])(testApi)