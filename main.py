import os
from dotenv import load_dotenv
load_dotenv()


from flask import Flask

from config import db
from routes.atributo_bp import attribute_bp
from routes.dimensao import dimension_bp
from routes.formulario import form_bp
from routes.pergunta import question_bp
from routes.tdd import tdd_bp
from flask_cors import CORS
# from webapp import app
import click


@click.group()
def cli():
    pass


@cli.command()
@click.option('-a', '--address', type=str, default='0.0.0.0')
@click.option('-p', '--port', type=int, default=5000)
@click.option('-d', '--debug', type=bool, default=True)


def create_app():


    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("API_BD_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    app.register_blueprint(attribute_bp)
    app.register_blueprint(dimension_bp)
    app.register_blueprint(question_bp)
    app.register_blueprint(tdd_bp)
    app.register_blueprint(form_bp)

    CORS(app)

    db.init_app(app)
    with app.app_context():
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run()