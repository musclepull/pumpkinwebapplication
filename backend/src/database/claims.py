from uuid import UUID

from src.database.db import Session
from src.models import Claim
from src.models import ClaimLineItem
from src.models import Utilization

def get_claims():
    return Session.query(Claim).all()

def get_claims_for_id(claim_id: UUID):
    return Session.query(Claim).filter(Claim.id == claim_id)

def get_items_from_claim_id(claim_id: UUID):
    return Session.query(ClaimLineItem).join(Claim).filter(Claim.id == claim_id)

def get_claim_item_for_id(claim_item_id: UUID):
    return Session.query(ClaimLineItem).filter(ClaimLineItem.id == claim_item_id)

def get_all_utilization():
    return Session.query(Utilization).all()

def get_utilization(claim_id, line_item_id):
   return Session.query(Utilization).join(ClaimLineItem).join(Claim).filter(ClaimLineItem.id == line_item_id, Claim.id == claim_id)

def delete_utilization(id):
   Session.query(Utilization).filter(Utilization.id == id).delete()
   Session.commit()


def update_claim(_id: UUID, _decision):
    Session.query(ClaimLineItem).filter(ClaimLineItem.id == _id).update({'decision': _decision})
    Session.commit()

def add_utilization(line_item_id, quantity):
    u1 = Utilization(claim_line_items_id = line_item_id, utilized = quantity, total = 100)
    Session.add(u1)
    Session.commit()

def update_utilization(_id, quantity):
    Session.query(Utilization).filter(Utilization.id == _id).update({'utilized': quantity})
    Session.commit()