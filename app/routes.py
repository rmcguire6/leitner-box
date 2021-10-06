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

@app.route('/create_card', methods=['POST'])
def create_card():
    user_id = request.args.get('user_id')
    if user_id:
        user_id = int(user_id)
        test = models.User.query.filter_by(user_id=user_id)
        if test:
            subject = request.json['subject']
            question = request.json['question']
            answer = request.json['answer']
            card = models.Card(subject=subject, question=question, answer=answer, user_id=user_id)
            db.session.add(card)
            db.session.commit()
            return jsonify(message="Card created successfully."), 201
        else: return jsonify(message="Card can not be created."), 409
    else:
        return jsonify(message="Card can not be created."), 409
