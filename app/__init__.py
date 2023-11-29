from flask import Flask
from flask_migrate import Migrate

from .src.controller import api
from .src.model import db

# app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

def create_app():
    app = Flask(__name__)

    # Banco de Dados
    # app.config.from_object('config')
    # db.init_app(app)
    # migrate = Migrate(app, db)

    # Registro de rotas
    app.register_blueprint(api)
    ## Caso quisesse registrar outras rotas por blueprint
    ## app.register_blueprint(outraBlueprint)
    return app
