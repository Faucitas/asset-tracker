import uuid

from flask import Blueprint, jsonify, abort, request
from api.account.models import Account, AccountSchema

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
        return {"message": "you are not authorized to view this account"}
    return AccountSchema().dump(account)






