# Representa os dados e suas relações. Será a parte com integração ao Banco de Dados

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Cria a extensão
db = SQLAlchemy()

class Grades(db.Model):
    __tablename__ = "Grades"
    id            = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name          = db.Column(db.String(64), nullable=False)
    first_grade   = db.Column(db.Double, nullable=True, default=0.0)
    second_grade  = db.Column(db.Double, nullable=True, default=0.0)
    created_at    = db.Column(db.DateTime(timezone=True), default=datetime.now)
    updated_at    = db.Column(db.DateTime(timezone=True), default=datetime.now, onupdate=datetime.now)

    # Campo utilizado como identificador do registro para poder apresentar objeto como string.
    # Ex. Se mandar print(grade) e estiver em Json retorno será, por exemplo : <Grades Eduardo>
    def __repr__(self):
        return f"<Grades {self.name}>"

    # Atributo to_dictionary necessário para serializar o Json e devolver como resposta (análogo ao ByteString no Haskell)
    # https://stackoverflow.com/questions/5022066/how-to-serialize-sqlalchemy-result-to-json/46180522#46180522
    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
