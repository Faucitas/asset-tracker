from flask import Flask
from flask_migrate import Migrate
# from model.user import User


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost:5432/asset_tracker'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from database import db
    migrate = Migrate(app, db)

    return app

if __name__ == '__main__':
    app = create_app()
    # db.init_app(app)
    app.run(port=5000, debug=True)