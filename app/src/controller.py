# Arquivo com as rotas e suas definições
# Se mantém entre a view e model

from flask import Blueprint, request, jsonify

from .model import db, Grades

# Nesse caso fico todas rotas referentes ao Site. Caso queira rotas para outro serviço, criar novo arquivo e nomear de forma parecida.
# url_prefix -> permite acessar endpoints a partir daquele prefix
api = Blueprint("api", __name__, url_prefix="/")

## ROTAS

# Rota inicial
@api.route("/")
def index():
    return "Welcome to the home page!"

# GET -- OK
@api.route("/grades/<grade_id>", methods=["GET"])
def gradesRouteShow(grade_id):
    # Faz a query no banco e tranforma resultado em dicionário Python.
    response = Grades.query.get(grade_id).to_dict()

    # Devolve JSON do dicionário.
    return jsonify(response)
    # return "Retorna JSON da nota"

# INSERT -- OK
@api.route("/grades", methods=["POST"])
def gradesRouteCreate():
    # Recebe request Json
    request_json = request.get_json()

    # Dá para pegar o content type para tratar casos de envio de requests não Json
    # content_type = request.headers.get("Content-Type")

    # Construção do registro a ser adicionado.
    new_grades = Grades(
                        #   id         -> Inserido automáticamente pelo banco de dados.
                        #   created_at -> Inserido automáticamente pelo banco de dados.
                        #   updated_at -> Inserido automáticamente pelo banco de dados.
                          name         = request_json.get("name"),
                          first_grade  = request_json.get("first_grade", 0.0),
                          second_grade = request_json.get("second_grade", 0.0)
                          )
    
    # Envia a request de inserção e manda operação ser executada
    db.session.add(new_grades)
    db.session.commit()

    # Devolve uma resposta para o View informar sobre operação
    response = Grades.query.get(new_grades.id).to_dict()
    return jsonify(response)
    # return "Adiciona uma nova Nota"

# DELETE -- OK
@api.route("/grades/<grade_id>", methods=["DELETE"])
def gradesRouteDelete(grade_id):
    # Salva registro para apresentar o que foi deletado.
    # Obs. O Grades.query gera a query a ser executada, se não colocar to_dict() e fazê-lo depois do commit
    # ele irá buscar no banco e não encontrará.
    gradeRemoved = Grades.query.get(grade_id).to_dict()

    # Faz a query de remoção de registro com id informado e efetiva a remoção. Executa a query em seguida.
    Grades.query.filter_by(id=grade_id).delete()
    db.session.commit()

    # Retorna o registro removido como resposta.
    return ("Registro Removido : {}\n").format(gradeRemoved)
    # return "Remove uma nova Nota"

# UPDATE -- OK.
# Há a possibilidade de buscar o registro pelo nome e atualizar, e não pelo ID gerado automaticamente.
@api.route("/grades/<grade_id>", methods=["PUT"])
def gradesRouteUpdate(grade_id):
    # Recebe request Json
    request_json = request.get_json()
    # Resgata registro a atualizar
    old_grades = Grades.query.get(grade_id)

    print(old_grades)

    # Atualiza cada campo.
    old_grades.name         = request_json.get("name") 
    old_grades.first_grade  = request_json.get("first_grade", old_grades.first_grade)
    old_grades.second_grade = request_json.get("second_grade", old_grades.second_grade)

    # Efetua as mudançar, executando a query.
    db.session.commit()

    # Retorna o registro atualizado 
    response = Grades.query.get(grade_id).to_dict()
    return jsonify(response)

    # return "Atualiza uma nova nota."

# GETALL -- OK
@api.route("/grades", methods=["GET"])
def gradesAllRouteShow():
    # Query para pegar todos registros.
    all_grades = Grades.query.all()
    # lista que comporá a resposta devolvida.
    response = []
    # Anexa o resultado da Query. Necessário serializar o resultado e converter para o formato do JSON.
    for grades in all_grades: response.append(grades.to_dict())
    # Devolve JSON dos registros.
    return jsonify(response)
    # return "Lista todas as notas."