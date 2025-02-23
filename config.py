import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Usa PostgreSQL si está en Heroku, de lo contrario usa SQLite localmente
DATABASE_URL = os.getenv("DATABASE_URL")
if DATABASE_URL:
    SQLALCHEMY_DATABASE_URI = DATABASE_URL.replace("postgres://", "postgresql://")
else:
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "instance", "mi_api.db")

SQLALCHEMY_TRACK_MODIFICATIONS = False
 
    