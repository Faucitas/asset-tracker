import uuid

from flask import Blueprint, jsonify, abort, request
from marshmallow import ValidationError
from api.user.models import User
from api.transaction.models import Account, AccountSchema


bp = Blueprint('accounts', __name__, url_prefix='/accounts')


@bp.route('', methods=['GET'])
def index():
    body = request.json
    if 'user_id' not in body:
        return abort(400)
    accounts = Account.get_all(**body)
    result = AccountSchema(many=True).dump(accounts)
    return jsonify(result)


@bp.route('/<uuid:account_id>', methods=['GET'])
def show(account_id: uuid):
    body = request.json
    if 'user_id' not in body:
        return abort(400)

    account = Account.get(account_id)
    if account.get_user() != body['user_id']:
        return {"message": "you are not authorized to view this transaction"}
    return AccountSchema().dump(account)


@bp.route('', methods=['POST'])
def create():
    body = request.json
    schema = AccountSchema()
    try:
        result = schema.load(body)
    except ValidationError as err:
        return  jsonify(err.messages), 400

    new_account = Account.create(**result)
    return schema.dump(new_account), 201


@bp.route('/<uuid:account_id>', methods=['PUT'])
def update(account_id: uuid):
    body = request.json
    schema = AccountSchema(partial=True)
    try:
        schema.load(body)
    except ValidationError as err:
        return jsonify(err.messages), 400

    account = Account.query.filter_by(user_id=body['user_id'], id=account_id).first_or_404()
    account.update(**body)
    return schema.dump(account)


@bp.route('/<uuid:account_id>', methods=['DELETE'])
def delete(account_id: uuid):
    body = request.json
    account = Account.query.filter_by(user_id=body['user_id'], id=account_id).first_or_404()
    account_name = account.get_attribute('name')
    account.delete()
    return jsonify({"message": f"Deleted {account_name}"}), 200

