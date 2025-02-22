from flask_cors import CORS
from flask import Flask, request, jsonify
from models.models import db, Freelancer, Company

# 🔹 Inicializar Flask
app = Flask(__name__)
CORS(app)  # Permitir acceso desde cualquier origen (Wix)

# 🔹 Configurar la base de datos SQLite
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///instance/mi_api.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)  # ✅ Inicializar db correctamente

# 🔹 Crear la base de datos dentro del contexto de la aplicación
with app.app_context():
    db.create_all()

# 🔹 Ruta principal de prueba
@app.route("/")
def home():
    return jsonify(mensaje="¡La API está funcionando correctamente!")


# 🔹 Ruta para registrar un freelancer
@app.route("/register", methods=["POST"])
def register_freelancer():
    print("🔹 [FREELANCER] Headers recibidos:", request.headers)  
    print("🔹 [FREELANCER] Contenido recibido:", request.data)  

    if request.content_type != "application/json":
        return jsonify({"error": "El Content-Type debe ser application/json"}), 415

    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No se enviaron datos"}), 400
    except Exception as e:
        return jsonify({"error": f"Error al procesar JSON: {str(e)}"}), 400

    nombre = data.get("nombre")
    email = data.get("email")
    skills = ", ".join(data.get("skills", []))

    if not nombre or not email or not skills:
        return jsonify({"error": "Faltan datos"}), 400

    # 🔹 Verificar si el email ya existe en la base de datos
    existente = Freelancer.query.filter_by(email=email).first()
    if existente:
        return jsonify({"error": "Este email ya está registrado"}), 409

    # 🔹 Si el email no existe, registrar freelancer
    nuevo_freelancer = Freelancer(nombre=nombre, email=email, skills=skills)
    db.session.add(nuevo_freelancer)
    db.session.commit()

    return jsonify({"mensaje": "Freelancer registrado exitosamente"}), 201


# 🔹 Ruta para registrar una empresa
@app.route("/register-company", methods=["POST"])
def register_company():
    print("🔹 [EMPRESA] Headers recibidos:", request.headers)  
    print("🔹 [EMPRESA] Contenido recibido:", request.data)  

    if request.content_type != "application/json":
        return jsonify({"error": "El Content-Type debe ser application/json"}), 415

    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No se enviaron datos"}), 400
    except Exception as e:
        return jsonify({"error": f"Error al procesar JSON: {str(e)}"}), 400

    nombre = data.get("nombre")
    email = data.get("email")
    rubro = data.get("rubro")
from routes.freelancer_routes import freelancer_routes
app.register_blueprint(freelancer_routes)
    

