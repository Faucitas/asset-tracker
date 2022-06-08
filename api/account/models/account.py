from api.database import Column, Model
from api.extentions import ma, db


class Account(Model):
    __tablename__ = 'accounts'
    account_number = Column(db.String(128), nullable=False)
    strategy = Column(db.String(128), nullable=True)
    custodian = Column(db.String(128), nullable=False)

    def get_attribute(self, attribute):
        value = getattr(self, attribute)
        return value


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Account

    account_number = ma.auto_field()
    strategy = ma.auto_field(required=False)
    custodian = ma.auto_field()
