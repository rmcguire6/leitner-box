from app import app
from app import db
from app import models
from flask import jsonify, request 

@app.route('/')
@app.route('/index')
def index():
    return "Hello World from Flask"

@app.route('/auth/register', methods=['POST'])
def create_user():
    if request.is_json:
        username = request.json['name']
        test = models.User.query.filter_by(username=username).first()
    if test:
        return jsonify(message="That user name is taken. Please try another one."), 409
    else:
        user = models.User(username = username)
        db.session.add(user)
        db.session.commit()
        return jsonify(message="User created successfully."), 201
