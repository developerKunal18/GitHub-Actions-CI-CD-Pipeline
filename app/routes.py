from flask import Blueprint, jsonify, request
from . import db
from .models import User, Product

api = Blueprint("api", __name__)

@api.get("/health")
def health():
    return jsonify(status="healthy")

@api.post("/users")
def create_user():
    data = request.get_json() or {}

    if not data.get("name"):
        return jsonify(error="Name required"), 400
    if not data.get("email"):
        return jsonify(error="Email required"), 400
    if User.query.filter_by(email=data["email"]).first():
        return jsonify(error="Email already exists"), 409

    user = User(name=data["name"], email=data["email"])
    db.session.add(user)
    db.session.commit()

    return jsonify(id=user.id, name=user.name, email=user.email), 201

@api.get("/products")
def products():
    return jsonify([
        {"id": p.id, "name": p.name, "price": p.price}
        for p in Product.query.all()
    ])
