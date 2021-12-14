
from typing import Dict
from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from flask_rest_api import Api
from src.config import EnvConfig
from src.schemas.claims import ClaimSchema, ResponseClaimSchema
from src.database import claims as orm
from src.models.exceptions.http_exceptions import HTTPResourceNotFound
from src.blueprints import claims_blueprint
from src.blueprints import utilization_blueprint
import uuid
import json
from functools import wraps

def create_app():
    app = Flask("Pumpkin Fullstack Test")

    app.config.from_object(EnvConfig())

    CORS(
        app,
        send_wildcard=True,
        expose_headers='Content-Range,Access-Control-Allow-Origin,Access-Control-Allow-Headers',
    )

    api = Api(app)
    api.register_blueprint(claims_blueprint.blueprint, url_prefix='/claims')
    api.register_blueprint(utilization_blueprint.blueprint, url_prefix='/utilization')

    return app

if __name__ == '__main__':
    app = create_app()
   

    @app.route('/claims/add', methods =['POST'])
    def add():
        request_data = request.get_json()
        line_item_id = request_data['id']
        claim_id = request_data['claim_id']
        quantity = request_data['quantity']
        orm.add_utilization(uuid.UUID(line_item_id))
        return "success"
 
    @app.route('/claims/update', methods =['POST'])
    def update():
        
        ## update claim
        request_data = request.get_json()
        benefit_type = request_data['claim_line_item_type']    
        line_item_id = uuid.UUID(request_data['id'])
        claim_id = uuid.UUID(request_data['claim_id'])
        quantity = request_data['quantity']
        claim = orm.get_claims_for_id(claim_id)
        if claim is None:
            return HTTPResourceNotFound
        orm.update_claim(line_item_id, request.json['decision'])

        ## update utilization

        utilization = orm.get_utilization(claim_id,line_item_id)
        if utilization.first() is None:
            # just to have something in the utilization table            
            #print('No Utilization Record...')
            orm.add_utilization(line_item_id, quantity)
            #print('Successfully Added Utilization Record...')
            
            add_utilization_dict = dict()
            add_utilization_dict['benefit_type'] = benefit_type
            add_utilization_dict['claim_id'] = request_data['claim_id']
            add_utilization_dict['line_item_id'] = request_data['id']
            add_utilization_dict['utilized'] = quantity
            add_utilization_dict['total'] = 100
            return add_utilization_dict
        else:
            #print('Successfully Obtained Utilization Record..') 
            updated_quantity = utilization.first().utilized + quantity
            orm.update_utilization(utilization.first().id, updated_quantity)
            #print('Successfully Updated Utilization Record...')

            updated_utilization_dict = dict()
            updated_utilization_dict['benefit_type'] = benefit_type
            updated_utilization_dict['claim_id'] = request_data['claim_id']
            updated_utilization_dict['line_item_id'] = request_data['id']
            updated_utilization_dict['utilized'] = updated_quantity
            updated_utilization_dict['total'] = utilization.first().total
            return updated_utilization_dict

    @app.route('/claims/delete', methods =['POST'])
    def delete():
        request_data = request.get_json()
        id = uuid.UUID(request_data['id'])
        orm.delete_utilization(id)
        return "success"


    # I'm using claim_id and item_id since an item_id can be replicated amongst various claims

    # @app.route('/claims/updateUtilization', methods =['POST'])
    # def updateUtilization():
    #     request_data = request.get_json()
    #     line_item_id = uuid.UUID(request_data['id'])
    #     claim_id = uuid.UUID(request_data['claim_id'])
    #     quantity = request_data['quantity']
    #     claim = orm.get_claims_for_id(claim_id)
    #     #print('claim_id: ' + request_data['id'])
    #     #print('line_item_id: ' + request_data['id'])
    #     #print('quantity: ' + str(quantity))
    #     if claim is None:
    #         return HTTPResourceNotFound
    #     claim_line_item  = orm.get_claim_item_for_id(line_item_id)
    #     #print('I have the line item: ' + request_data['id'])
    #     if claim_line_item is None:
    #         return HTTPResourceNotFound
    #     #print('Hitting Get Utilization method....')
    #     utilization = orm.get_utilization(claim_id,line_item_id)
    #     if utilization.first() is None:
    #         # just to have something in the utilization table            
    #         #print('No Utilization Record...')
    #         orm.add_utilization(line_item_id)
    #         #print('Successfully Added Utilization Record...')      
    #     else:
    #         #print('Successfully Obtained Utilization Record..')      
    #         orm.update_utilization(utilization.first().id,quantity)
    #         #print('Successfully Updated Utilization Record...')
    #         new_updated_utilization_object = orm.get_utilization(claim_id,line_item_id)    
    #     return new_updated_utilization_object.first()

    app.run(port=8085, host='0.0.0.0', debug=True)
