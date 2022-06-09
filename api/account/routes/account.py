import uuid

from flask import Blueprint, jsonify, abort, request
from marshmallow import ValidationError
from api.user.models import User
from api.account.models import Account, AccountSchema


bp = Blueprint('accounts', __name__, url_prefix='/accounts')


@bp.route('', methods=['GET'])
def index():
    accounts = Account.get_all()
    result = AccountSchema(many=True).dump(accounts)
    return jsonify(result)


@bp.route('/<uuid:account_id>', methods=['GET'])
def show(account_id: uuid):
    account = Account.get(account_id)
    result = AccountSchema().dump(account)
    print(result)

    return jsonify(result)


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

    account = Account.get(account_id)
    account.update(**body)
    return schema.dump(account)


@bp.route('/<uuid:account_id>', methods=['DELETE'])
def delete(account_id: uuid):
    account = Account.get(account_id)
    account_custodian = account.get_attribute('custodian')
    account.delete()
    return jsonify({"message": f"Deleted {account_custodian}"}), 200

