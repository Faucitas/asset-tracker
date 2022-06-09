from api.database import Column, PKModel
from api.extentions import ma, db


class User(PKModel):
    __tablename__ = 'users'
    username = Column(db.String(128), unique=True, nullable=False)
    password = Column(db.String(256), nullable=False)
    email = Column(db.String(128))
    is_admin = Column(db.Boolean, default=False, nullable=False)

    def get_attribute(self, attribute):
        value = getattr(self, attribute)
        return value


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User

    id = ma.auto_field()
    username = ma.auto_field(required=False)
    email = ma.auto_field()
    password = ma.auto_field(load_only=True)
