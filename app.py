from flask import Flask, jsonify
from flask_cors import CORS
from models.models import db
import os

# 🔹 Inicializar la aplicación Flask
app = Flask(__name__)
CORS(app)  # Habilitar CORS para permitir conexiones externas

# 🔹 Configurar base de datos SQLite
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///instance/mi_api.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# 🔹 Inicializar la base de datos
db.init_app(app)
with app.app_context():
    db.create_all()

# 🔹 Ruta principal de prueba
@app.route("/")
def home():
    return jsonify({"mensaje": "API funcionando correctamente en Heroku"}), 200

# 🔹 Ruta de estado para pruebas
@app.route("/status")
def status():
    return jsonify({"status": "API en línea"}), 200

# 🔹 Ruta para registrar freelancers
@app.route("/register", methods=["POST"])
def register_freelancer():
    from flask import request

    data = request.get_json()
    if not data:
        return jsonify({"error": "No se enviaron datos"}), 400

    nombre = data.get("nombre")
    email = data.get("email")
    skills = ", ".join(data.get("skills", []))

    if not nombre or not email or not skills:
        return jsonify({"error": "Faltan datos"}), 400

    # Verificar si el email ya existe en la base de datos
    existente = Freelancer.query.filter_by(email=email).first()
    if existente:
        return jsonify({"error": "Este email ya está registrado"}), 409

    # Si el email no existe, registrar freelancer
    nuevo_freelancer = Freelancer(nombre=nombre, email=email, skills=skills)
    db.session.add(nuevo_freelancer)
    db.session.commit()

    return jsonify({"mensaje": "Freelancer registrado exitosamente"}), 201

# 🔹 Iniciar la aplicación en el puerto correcto en Heroku
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Obtener el puerto que asigna Heroku
    app.run(host='0.0.0.0', port=port)



