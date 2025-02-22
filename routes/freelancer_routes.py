from flask import Blueprint, jsonify
from models.models import db, Freelancer

freelancer_routes = Blueprint('freelancer_routes', __name__)

# 🔹 Endpoint para listar todos los freelancers
@freelancer_routes.route("/freelancers", methods=["GET"])
def get_freelancers():
    freelancers = Freelancer.query.all()
    freelancers_list = [
        {"id": f.id, "nombre": f.nombre, "email": f.email, "skills": f.skills}
        for f in freelancers
    ]
    return jsonify(freelancers_list), 200
 
