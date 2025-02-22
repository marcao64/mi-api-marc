from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# 🔹 Modelo para Freelancer
class Freelancer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    skills = db.Column(db.String(200), nullable=False)

# 🔹 Modelo para Company
class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    rubro = db.Column(db.String(200), nullable=False)

 
