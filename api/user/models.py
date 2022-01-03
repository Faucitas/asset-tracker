from api.database import db, Column, Model
from api.extentions import ma

class User(Model):
    __tablename__ = 'users'
    username = Column(db.String(128), unique=True, nullable=False)
    password = Column(db.String(128), nullable=False)
    email = Column(db.String(128))
    is_admin = Column(db.Boolean, default=False, nullable=False)

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get(cls, user_id):
        return cls.query.get_or_404(user_id)


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User

    id = ma.auto_field()
    username = ma.auto_field()
    email = ma.auto_field()

