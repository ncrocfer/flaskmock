from flask import Flask, jsonify, Blueprint, request

from myproject.controllers.sources import SourceController
from myproject.extensions import db

api = Blueprint('apiv1', __name__)


def format_source(obj):
    return {
        'id': obj.id,
        'name': obj.name,
        'createdAt': obj.created_at,
        'updatedAt': obj.updated_at
    }


@api.route('/sources', methods=['GET'])
def list_sources():
    sources = [
        format_source(s)
        for s in SourceController.list()
    ]
    return jsonify(sources), 200


@api.route('/sources', methods=['POST'])
def create_source():
    payload = request.get_json(force=True)
    source = SourceController.create(payload)
    return jsonify(format_source(source)), 200


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    db.init_app(app)
    app.register_blueprint(api)
    return app
