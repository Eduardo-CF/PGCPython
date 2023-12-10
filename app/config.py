# Configurações gerais do serviço

import os

# Diretorio onde se encontra o config.py
basedir = os.path.abspath(os.path.dirname(__file__))

# URI para o SQLite
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "database.db")

# Habilita o modo de Debug
DEBUG = True

# Valor aleatório caso seja necessário
SECRET_KEY = os.urandom(32)