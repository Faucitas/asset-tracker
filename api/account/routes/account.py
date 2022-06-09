import uuid

from flask import Blueprint, jsonify, abort, request
from marshmallow import ValidationError
from api.user.models import User
from api.account.models import Account, AccountSchema


bp = Blueprint('accounts', __name__, url_prefix='/accounts')

