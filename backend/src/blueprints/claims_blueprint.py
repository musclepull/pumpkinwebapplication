from src.models.claim_line_item import ClaimLineItem
from flask import Flask, request, jsonify, make_response
from flask_rest_api import Blueprint
from flask.views import MethodView
from src.database import claims as orm
from src.models.exceptions.http_exceptions import HTTPResourceNotFound
from src.schemas.claims import ResponseClaimSchema
from src.schemas.claim_line_items import ClaimLineItemSchema
from src.schemas.utilizations import UtilizationSchema
from src.schemas.claim_line_items import ClaimLineItemResponse
import uuid

blueprint = Blueprint(
    'claims', 
    'utilization',
    __name__
)

@blueprint.route("", methods=['GET'])
class NotesView(MethodView):

    @blueprint.response(schema=ResponseClaimSchema(many=True))
    def get(self):
        claim = orm.get_claims()    
        return claim
    
@blueprint.route("/<uuid:claim_id>", methods=['GET'])
class NotesView(MethodView):

    @blueprint.response(schema=ResponseClaimSchema(many=True))
    def get(self, claim_id):
        claim = orm.get_claims_for_id(claim_id)
        if claim is None:
            raise HTTPResourceNotFound
        return claim

@blueprint.route("<uuid:claim_id>/utilization", methods=['GET'])
class NotesView(MethodView):
    def get(self,claim_id):
        utilization = orm.get_items_from_claim_id(claim_id)  
        List = []

        for obj in utilization:
            utilization_dict = dict()
            print('Claim ID: ' + str(claim_id))
            print('line_item_util: ' + str(obj.id))

            line_item_util = orm.get_utilization(claim_id, obj.id)

            if obj.claim_line_item_type == ClaimLineItem.ClaimLineItemTypeEnum.vaccine: 
                utilization_dict['claim_line_item_type'] =  "Vaccine"
            elif obj.claim_line_item_type == ClaimLineItem.ClaimLineItemTypeEnum.blood_test: 
                utilization_dict['claim_line_item_type'] =  "Blood Test"
            else:
                utilization_dict['claim_line_item_type'] =  "Wellness Exam"


            utilization_dict['claim_id'] = claim_id
            utilization_dict['line_item_id'] = obj.id
            if line_item_util.first() is None:
                utilization_dict['utilized'] = 0
            else:
                 utilization_dict['utilized'] = line_item_util.first().utilized
            if line_item_util.first() is None:
                utilization_dict['total'] = 0
            else:
                 utilization_dict['total'] = line_item_util.first().total

            List.append(utilization_dict)
            

        list_d = dict()

        list_d["data"] = List

        return list_d

@blueprint.route("<uuid:claim_id>/utilization/<uuid:item_id>/", methods=['GET'])
class NotesView(MethodView):
    @blueprint.response(schema=UtilizationSchema(many=True))
    def get(self,claim_id, item_id):
        utilization = orm.get_utilization(claim_id,item_id)    
        return utilization



