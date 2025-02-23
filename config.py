import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Cambia a PostgreSQL si la variable DATABASE_URL está configurada en Heroku
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///" + os.path.join(BASE_DIR, "instance", "mi_api.db")).replace("postgres://", "postgresql://")

SQLALCHEMY_TRACK_MODIFICATIONS = False

SQLALCHEMY_TRACK_MODIFICATIONS = False
import os

SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "").replace("postgres://", "postgresql://")
SQLALCHEMY_TRACK_MODIFICATIONS = False

 
