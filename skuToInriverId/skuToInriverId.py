from datetime import datetime
import json
import os
from google.cloud import firestore


def sendSlackMessage(request):
    # prep response object
    responseDict = {'data': {}}
    # parse request
    request_json = request.get_json()
    # authenticate
    if request_json['api_key'] != os.environ["gcloudAPIKey"]:
        return('Access Denied')
    #####

    # type checking
    if type(request_json['skus']) != list:
        return('Array of strings not sent.')

    db = firestore.Client()
    inRiverScrape = db.collection('sku-inriver-translation-table')

    for sku in request_json['skus']:
        try:
            entID = inRiverScrape.document(
                str(sku)).get().to_dict()['entityID']
            responseDict['data'][sku] = entID
        except:
            responseDict['data'][sku] = False

    responseDict = json.dumps(responseDict)
    return(responseDict)
