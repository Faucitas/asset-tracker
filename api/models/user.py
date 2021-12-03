from flask import jsonify
from app import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128))

    # def __init__(self, name, password, email=None):
    #     self.name = name
    #     self.password = password
    #     self.email = email

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }

    @classmethod
    def get_all_users(cls):
        users = cls.query.all()
        results = []
        for user in users:
            results.append(user.serialize())
        return jsonify(results)

    @classmethod
    def get_user(cls, user_id: int):
        user = cls.query.get_or_404(user_id)
        return jsonify(user.serialize())


