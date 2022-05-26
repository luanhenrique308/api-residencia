from flask import Flask

from config import db
from routes.atributo_bp import atributo_bp
from routes.dimensao import dimension_bp
from routes.pergunta import question_bp
from routes.tdd import tdd_bp


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:32553964@localhost/residencias'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.secret_key = '32553964'

    app.register_blueprint(atributo_bp)
    app.register_blueprint(dimension_bp)
    app.register_blueprint(question_bp)
    app.register_blueprint(tdd_bp)

    db.init_app(app)
    with app.app_context():
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    #app.debug = True
    app.run()