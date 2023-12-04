# Arquivo com as rotas e suas definições
# Se mantém entre a view e model

from flask import Blueprint
from .model import db

# Nesse caso fico todas rotas referentes ao Site. Caso queira rotas para outro serviço, criar novo arquivo e nomear de forma parecida.
# url_prefix -> permite acessar endpoints a partir daquele prefix
api = Blueprint('api', __name__, url_prefix='/')

## ROTAS


@api.route('/')
def index():
    return 'Welcome to the home page!'

@api.route('/grades/<id>', methods=['GET'])
def gradesRouteShow(id):
    return 'Retornar JSON da nota'

@api.route('/grades', methods=['POST'])
def gradesRouteCreate():
    return 'Adicionar uma nova Nota'

@api.route('/grades/<id>', methods=['DELETE'])
def gradesRouteDelete(id):
    return 'Remove uma nova Nota'

@api.route('/grades/<id>', methods=['PUT'])
def gradesRouteUpdate(id):
    return 'Atualiza uma nova Nota'

@api.route('/grades', methods=['GET'])
def gradesAllRouteShow():
    return 'Lista todas as notas !'