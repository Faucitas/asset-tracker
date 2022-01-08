from api.database import Column, Model
from sqlalchemy.dialects.postgresql import UUID
from . import db
from api.extentions import ma


class Account(Model):
    __tablename__ = 'accounts'
    name = Column(db.String(80), unique=False, nullable=False)
    type = Column(db.String(80), unique=False, nullable=False)
    user_id = Column(UUID(as_uuid=True), db.ForeignKey('users.id'), nullable=False)


class AccountSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Account