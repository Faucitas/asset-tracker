from flask import Blueprint, jsonify, abort, request
from api.user.models import User

bp = Blueprint('users', __name__, url_prefix='/users')


@bp.route('/', methods=['GET'])
def index():
    users = User.get_all()
    return jsonify(users), 200


@bp.route('/<int:user_id>', methods=['GET'])
def show(user_id: int):
    user = User.get_or(user_id)
    return jsonify(user), 200


@bp.route('/', methods=['POST'])
def create():
    body = request.json
    if 'username' not in body or 'password' not in body:
        print('end here')
        return abort(400)
    user = User.create(**body)
    return jsonify(user.serialize())