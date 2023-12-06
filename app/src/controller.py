# Arquivo com as rotas e suas definições
# Se mantém entre a view e model

from flask import Blueprint, request, jsonify
import uuid

from .model import db, GradesTable

# Nesse caso fico todas rotas referentes ao Site. Caso queira rotas para outro serviço, criar novo arquivo e nomear de forma parecida.
# url_prefix -> permite acessar endpoints a partir daquele prefix
api = Blueprint('api', __name__, url_prefix='/')

## ROTAS


@api.route('/')
def index():
    return 'Welcome to the home page!'

# GET
@api.route('/grades/<id>', methods=['GET'])
def gradesRouteShow(id):
    response = GradesTable.query.get(id)
    print(response)
    return jsonify(response)
    # return 'Retornar JSON da nota'

# INSERT
@api.route('/grades', methods=['POST'])
def gradesRouteCreate():
    # Recebe request Json
    requestJson = request.get_json()

    # def optional(param):
    #     if not param:
    #         return None
    #     else: 
    #         return param


    # Dá para pegar o content type para tratar casos de envio de requests não Json
    # content_type = request.headers.get('Content-Type')

    # Gera id - Haskell gerou automático
    id = str(uuid.uuid4())
    # Construção do registro a ser adicionado ("Parsing")
    new_account = GradesTable(
                        #   id          = id,
                          name        = requestJson['name'],
                          firstGrade  = requestJson['firstGrade'],
                          secondGrade = requestJson['secondGrade']
                        #   firstGrade  = optional(requestJson['firstGrade']),
                        #   secondGrade = optional(requestJson['secondGrade'])
                          )
    
    # envia a request de inserção e manda operação ser executada
    db.session.add(new_account)
    db.session.commit()

    # Devolve uma resposta para o View informar sobre operação
    response = GradesTable.query.get(id)
    return jsonify(response)
    # return jsonify(requestJson)

    # return 'Adicionar uma nova Nota'

# DELETE
@api.route('/grades/<id>', methods=['DELETE'])
def gradesRouteDelete(id):
    return 'Remove uma nova Nota'

# UPDATE
@api.route('/grades/<id>', methods=['PUT'])
def gradesRouteUpdate(id):
    return 'Atualiza uma nova Nota'

# GETALL
@api.route('/grades', methods=['GET'])
def gradesAllRouteShow():
    return 'Lista todas as notas !'