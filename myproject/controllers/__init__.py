from myproject.extensions import db


class Controller(object):
    model_cls = None

    @classmethod
    def list(cls):
        return cls.model_cls.query.all()

    @classmethod
    def create(cls, data):
        obj = cls.model_cls(**data)
        db.session.add(obj)
        db.session.commit()
        return obj
