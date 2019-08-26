from google.cloud import firestore
from datetime import datetime
import json

def getSkuData(request):
    db = firestore.Client()
    responseDict = {}
    request_json = request.get_json()
    if request_json['sku'].find(',') > 0:
        skus = request_json['sku'].split(',')
    else:
        skus = [request_json['sku']]
    for sku in skus:
        doc = db.collection('ls-restful-api-scrape').document(sku).get()
        responseDict[doc.id] = doc.to_dict()
    response_dict = json.dumps(responseDict)
    return(response_dict)
