from flask import jsonify, request
from app import app
from app import db
from app.models import User, Card, cards_schema, users_schema

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/index')
def index():
    return "Hello World from Flask"

@app.route('/auth/register', methods=['POST'])
def create_user():
    if request.is_json:
        username = request.json['name']
        cards_per_day = int(request.json['cards_per_day'])
        test = User.query.filter_by(username=username).first()
        if test:
            return jsonify(message="That user name is taken. Please try another one."), 409
        else:
            user = User(username = username, cards_per_day=cards_per_day)
            db.session.add(user)
            db.session.commit()
            return jsonify(message="User created successfully."), 201
    else:
        return jsonify(message="Bad request"), 400

@app.route('/auth/login', methods=['POST'])
def login_user():
    if request.is_json:
        username = request.json['name']
        test = User.query.filter_by(username=username).first()
    if test:
        return jsonify(test.user_id)
    else:
        return jsonify(message="No user with that name."), 401


@app.route('/create_card', methods=['POST'])
def create_card():
    if request.is_json:
        _id = request.json['user_id']
    if _id:
        user_id = int(_id)
        test = User.query.filter_by(user_id=user_id)
        if test:
            subject = request.json['subject']
            question = request.json['question']
            answer = request.json['answer']
            card = Card(subject=subject, question=question, answer=answer, user_id=user_id)
            db.session.add(card)
            db.session.commit()
            return jsonify(message="Card created successfully."), 201
        else: return jsonify(message="Card can not be created."), 401
    else:
        return jsonify(message="Card can not be created."), 404

@app.route('/testing/cards', methods=['GET'])
def get_cards():
    cards = Card.query.all()
    result = cards_schema.dump(cards)
    return jsonify(result)

@app.route('/testing/users', methods=['GET'])
def get_users():
    users = User.query.all()
    result = users_schema.dump(users)
    return jsonify(result)
