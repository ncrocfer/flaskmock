import uuid

from sqlalchemy_utils import UUIDType

from myproject.extensions import db


def get_uuid():
    return str(uuid.uuid4())


def get_now():
    return db.func.now()


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(UUIDType(binary=False), primary_key=True, nullable=False, default=get_uuid)
    created_at = db.Column(db.DateTime(timezone=True), default=get_now(), nullable=False, index=True)
    updated_at = db.Column(db.DateTime(timezone=True), default=get_now(), onupdate=get_now(), nullable=False)
