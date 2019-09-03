from google.cloud import firestore
from datetime import datetime
import json


def getSkuData(request):
    db = firestore.Client()
    responseDict = {'data': {}}
    request_json = request.get_json()
    if request_json['sku'].find(',') > 0:
        skus = request_json['sku'].split(',')
    else:
        skus = [request_json['sku']]
    if len(skus) > 1000:
        skus = skus[:1000]
    for sku in skus:
        try:
            doc = db.collection('ls-restful-api-scrape').document(sku).get()
            responseDict['data'][str(doc.id)] = doc.to_dict()
        except:
            responseDict['data'][str(sku)] = 'Not found'
    response_dict = json.dumps(responseDict)
    return(response_dict)
