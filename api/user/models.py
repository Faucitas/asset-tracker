from api.database import db, Column, Model

class User(Model):
    __tablename__ = 'users'
    # id = Column(db.Integer, primary_key=True, autoincrement=True)
    username = Column(db.String(128), unique=True, nullable=False)
    password = Column(db.String(128), nullable=False)
    email = Column(db.String(128))
    is_admin = Column(db.Boolean, default=False, nullable=False)

    @classmethod
    def get_all(cls):
        users = cls.query.all()
        results = []
        for user in users:
            results.append(user.serialize())
        return results

    # @classmethod
    # def get(cls, user_id: int):
    #     user = cls.query.get_or_404(user_id)
    #     return user.serialize()

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }
