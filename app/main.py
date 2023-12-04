from flask import Flask
from flask_migrate import Migrate

from src.controller import api
from src.model import db, GradesTable

def create_app():
    app = Flask(__name__)

    # Resgata valor do config.py para saber se há a possibilidade de executar em modo Debug.
    app.debug

    ### Banco de Dados

    # Resgata o URI do arquivo config.py
    app.config.from_object('config')

    # O mesmo que acima sem o arquivo config.py:
    # #basedir = os.path.abspath(os.path.dirname(__file__))
    # #app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
    
    db.init_app(app)

    ### Registro de rotas
    
    app.register_blueprint(api)

    ## Caso quisesse registrar outras rotas por blueprint
    ## app.register_blueprint(outraBlueprint)

    return app

app = create_app()
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)

    