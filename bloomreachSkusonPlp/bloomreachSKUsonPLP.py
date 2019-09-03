from bs4 import BeautifulSoup
import requests
import json
import re
import math
import os
from google.cloud import firestore

db = firestore.Client()


def getSKUsFromPLP(request):
    request_json = request.get_json()
    if request_json['api_key'] != os.environ["gcloudAPIKey"]:
        return('Access Denied')
    skus = ""
    url = str(request_json['url'])
    docs = db.collection(
        "website-taxonomy-data").where("URL", "==", url).stream()
    for doc in docs:
        skus = doc.to_dict()['SKUs on Page']
    skus = list(dict.fromkeys(skus))
    return_data = {
        "data": {
            "skus": skus
        }
    }
    return_data = json.dumps(return_data)
    return(return_data)
