# Representa os dados e suas relações. Será a parte com integração ao Banco de Dados

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class GradesTable(db.Model):
    __tablename__ = 'Grades'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), nullable=False)
    firstGrade = db.Column(db.Double)
    secondGrade = db.Column(db.Double)

    # Campo utilizado como identificador do registro
    def __repr__(self):
        return f'<GradesTable {self.name}>'