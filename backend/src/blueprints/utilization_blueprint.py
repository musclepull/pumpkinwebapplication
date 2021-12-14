from flask import Flask, request, jsonify, make_response
from flask_rest_api import Blueprint
from flask.views import MethodView
from src.database import claims as orm
from src.models.exceptions.http_exceptions import HTTPResourceNotFound
from src.schemas.claims import ResponseClaimSchema
from src.schemas.utilizations import UtilizationSchema
import uuid

blueprint = Blueprint(
    'utilization',
    __name__
)

@blueprint.route("", methods=['GET'])
class NotesView(MethodView):

    @blueprint.response(schema=UtilizationSchema)
    def get(self):
        _claim_id  = uuid.UUID("7f94cd56-1247-4f62-9540-4806668018ee")
        _item_id  = uuid.UUID("02d29b81-d6ba-4e68-91d9-ab2047ef7736")
        utilization = orm.get_all_utilization()    
        return utilization
    




