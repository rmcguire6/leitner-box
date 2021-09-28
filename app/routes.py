from app import app
from app import models
from flask import jsonify

@app.route('/')
@app.route('/index')
def index():
    return "Hello World from Flask"

@app.route('/users')
def get_users():
    users_list = models.User.query.all()
    result = models.users_schema.dump(users_list[0])
    return jsonify(result)    

@app.route('/user/<int:user_id>', methods=["GET"])
def get_user(user_id: int):
    user = models.User.query.filter_by(user_id=user_id).first()
    if user:
        result = models.user_schema.dump(user)
        return jsonify(result)
    else:
        return jsonify(message="That user does not exist"), 404
