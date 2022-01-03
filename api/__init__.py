from flask import Flask
from api import user

from api.extentions import db, migrate, ma


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)


def register_blueprints(app):
    app.register_blueprint(user.routes.bp)

