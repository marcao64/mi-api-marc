from flask import Flask, request, jsonify

app = Flask(__name__)

# Datos de ejemplo (esto normalmente vendría de una base de datos)
freelancers = [
    {"id": 1, "nombre": "Ana", "skills": ["Python", "Django"]},
    {"id": 2, "nombre": "Juan", "skills": ["JavaScript", "React"]},
    {"id": 3, "nombre": "Sofía", "skills": ["Python", "Flask"]},
]

@app.route("/", methods=["GET"])
def home():
    return jsonify({"mensaje": "¡La API está funcionando correctamente!"})

@app.route("/match", methods=["POST"])
def match_freelancers():
    data = request.get_json()
    skills_requeridos = data.get("skills", [])
    
    # Filtra freelancers que tengan al menos uno de los skills requeridos
    candidatos = [f for f in freelancers if any(skill in f["skills"] for skill in skills_requeridos)]
    
    return jsonify({"matches": candidatos})

if __name__ == "__main__":
    app.run(debug=True)
