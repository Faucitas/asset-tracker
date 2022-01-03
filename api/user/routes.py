import uuid

from flask import Blueprint, jsonify, abort, request
from api.user.models import User, UserSchema

bp = Blueprint('users', __name__, url_prefix='/users')


@bp.route('', methods=['GET'])
def index():
    users = User.get_all()
    result = UserSchema(many=True).dump(users)
    return jsonify(result), 200


@bp.route('/<uuid: user_id>', methods=['GET'])
def show(user_id: uuid):
    user = User.get(user_id)
    return UserSchema().dump(user), 200


@bp.route('', methods=['POST'])
def create():
    body = request.json
    if 'username' not in body or 'password' not in body:
        return abort(400)

    user = User.create(**body)
    return UserSchema().dump(user), 200