from myproject.controllers import Controller
from myproject.models.sources import Source


class SourceController(Controller):
    model_cls = Source
