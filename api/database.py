from api.extentions import db
from sqlalchemy.dialects.postgresql import UUID
import uuid


# Common db aliases
Column = db.Column

class CRUDMixin(object):
    """
    Adds methods for CRUD (create, read, update, delete)
    """
    @classmethod
    def create(cls, **kwargs):
        instance = cls(**kwargs)
        return instance.save()

    def update(self, commit=True, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        if commit:
            return self.save()
        return self

    def save(self, commit=True):
        db.session.add(self)
        if commit:
            db.session.commit()
        return self

    def delete(self, commit=True):
        db.session.delete(self)
        if commit:
            return db.session.commit()
        return


class Model(CRUDMixin, db.Model):
    __abstract__ = True
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

