from flask import Blueprint, jsonify, abort, request
from api.models.user import User

users_api = Blueprint('users', __name__)


@users_api.route('/', methods=['GET'])
def index():
    users = User.get_all_users()
    return jsonify(users)


@users_api.route('/<int:user_id>', methods=['GET'])
def show(user_id: int):
    user = User.get_user(user_id)
    return jsonify(user), 200


@users_api.route('', methods=['POST'])
def create():
    body = request.json
    if 'username' not in body or 'password' not in body:
        return abort(400)

    return