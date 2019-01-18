from myproject.extensions import db
from myproject.models import BaseModel


class Source(BaseModel):

    __tablename__ = 'sources'
    name = db.Column(db.String(255), nullable=False)
