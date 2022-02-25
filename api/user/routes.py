import uuid
from flask import Blueprint, jsonify, abort, request
from marshmallow import ValidationError
# from flask_sqlalchemy import
from api.user.models import User, UserSchema

bp = Blueprint('users', __name__, url_prefix='/users')


@bp.route('/login', methods=['POST'])
def login():
    body = request.get_json()
    schema = UserSchema()

    try:
        data = schema.load(body)
    except ValidationError as err:
        return jsonify({'error': err.messages})

    user = User.query.filter_by(**data).first()
    if user:
        return schema.dump(user)
    return jsonify({'message': 'Bad Username or Password Entered'})


@bp.route('', methods=['GET'])
def index():
    users = User.get_all()
    result = UserSchema(many=True).dump(users)
    return jsonify(result), 200


@bp.route('', methods=['POST'])
def create():
    body = request.json
    if 'username' not in body or 'password' not in body:
        return abort(400)
    user = User.create(**body)
    return UserSchema().dump(user), 201


@bp.route('/<uuid:user_id>', methods=['GET'])
def show(user_id: uuid):
    user = User.get(user_id)
    return UserSchema().dump(user), 200


@bp.route('/<uuid:user_id>', methods=['DELETE'])
def delete(user_id: uuid):
    user = User.get(user_id)
    username = user.get_attribute('username')
    user.delete()
    return {"message": f"Deleted {username}"}, 200


@bp.route('/<uuid:user_id>', methods=['PUT'])
def update(user_id: uuid):
    body = request.json
    user = User.get(user_id)
    user.update(**body)
    return UserSchema().dump(user), 200