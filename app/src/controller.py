# Arquivo com as rotas e suas definições
# Se mantém entre a view e model

from flask import Blueprint, request, jsonify

from .model import db, Grades

# Nesse caso fico todas rotas referentes ao Site. Caso queira rotas para outro serviço, criar novo arquivo e nomear de forma parecida.
# url_prefix -> permite acessar endpoints a partir daquele prefix
api = Blueprint('api', __name__, url_prefix='/')

## ROTAS

# Rota inicial
@api.route('/')
def index():
    return 'Welcome to the home page!'

# GET -- OK
@api.route('/grades/<id>', methods=['GET'])
def gradesRouteShow(id):
    response = Grades.query.get(id).toDict()
    print(response)
    return jsonify(response)
    # return 'Retornar JSON da nota'

# INSERT -- OK
@api.route('/grades', methods=['POST'])
def gradesRouteCreate():
    # Recebe request Json
    requestJson = request.get_json()

    # Tentativa de utilizar uma função para validar no momento da construção do registro, porém não é possivel.
    # def optional(param):
    #     if not param:
    #         return None
    #     else: 
    #         return param

    # Dá para pegar o content type para tratar casos de envio de requests não Json
    # content_type = request.headers.get('Content-Type')

    # Construção do registro a ser adicionado ("Parsing")
    new_account = Grades(
                        # id -> Inserido automáticamente pelo banco de dados.
                          name        = requestJson['name'],
                          firstGrade  = requestJson['firstGrade'],
                          secondGrade = requestJson['secondGrade']
                          )
    
    # Envia a request de inserção e manda operação ser executada
    db.session.add(new_account)
    db.session.commit()

    # Devolve uma resposta para o View informar sobre operação
    response = Grades.query.get(new_account.id).toDict()
    return jsonify(response)
    # return 'Adicionar uma nova Nota'

# DELETE
@api.route('/grades/<id>', methods=['DELETE'])
def gradesRouteDelete(id):
    return 'Remove uma nova Nota'

# UPDATE
@api.route('/grades/<id>', methods=['PUT'])
def gradesRouteUpdate(id):
    return 'Atualiza uma nova Nota'

# GETALL -- OK
@api.route('/grades', methods=['GET'])
def gradesAllRouteShow():
    # Query para pegar todos registros.
    allGrades = Grades.query.all()
    # lista que comporá a resposta devolvida.
    response = []
    # Anexa o resultado da Query. Necessário serializar o resultado e converter para o formato do JSON.
    for grades in allGrades: response.append(grades.toDict())
    # Devolve JSON dos registros.
    return jsonify(response)
    # return 'Lista todas as notas !'