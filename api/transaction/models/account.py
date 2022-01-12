from api.database import Column, Model
from sqlalchemy.dialects.postgresql import UUID

from api.database import db
from api.extentions import ma


class Account(Model):
    __tablename__ = 'accounts'
    name = Column(db.String(80), unique=False, nullable=False)
    type = Column(db.String(80), unique=False, nullable=False)
    user_id = Column(UUID(as_uuid=True), db.ForeignKey('users.id'), nullable=False)

    def get_user(self):
        return str(self.user_id)


class AccountSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Account

    id = ma.auto_field()
    name = ma.auto_field()
    type = ma.auto_field()
    user_id = ma.auto_field()