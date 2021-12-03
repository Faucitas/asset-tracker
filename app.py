from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost:5432/asset_tracker'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    # Import models
    from api.models.user import User

    # Register Blueprints
    from api.routes.users import users_api
    app.register_blueprint(users_api, url_prefix='/users')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(port=5000, debug=True)