from flask import Flask, request, jsonify
from flask_cors import CORS
from models.models import db, Freelancer, Company
import os  # ⬅ Importar módulo para leer variables de entorno

# 🔹 Inicializar Flask
app = Flask(__name__)
CORS(app)

# 🔹 Configurar la base de datos
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///instance/mi_api.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

# 🔹 Crear la base de datos dentro del contexto de la aplicación
with app.app_context():
    db.create_all()

# 🔹 Ruta principal para verificar que la API está en línea
@app.route("/")
def home():
    return jsonify({"mensaje": "¡La API está funcionando correctamente en Heroku!"})

# 🔹 Ruta de estado para pruebas
@app.route("/status")
def status():
    return jsonify({"status": "API funcionando correctamente"})

# 🔹 Definir el puerto de Heroku
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # ⬅ Heroku asigna el puerto automáticamente
    app.run(host="0.0.0.0", port=port)





