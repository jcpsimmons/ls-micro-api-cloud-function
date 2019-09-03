from bs4 import BeautifulSoup
import requests
import json
import re
import math


def getSKUsFromPLP(request):
    request_json = request.get_json()
    url = request_json['url']
    if request_json['page']:
        page = request_json['page']
    else:
        page = 1
    if page == 1:
        start = 0
    elif page > 1:
        start = ((page - 1) * 5000) + 1
    pdps = []
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "html.parser")
    apiURL = soup.find('input', {'name': '_br_api_request'})[
        'value']
    apiURL = apiURL.replace("account_id=x", "account_id=5221").replace(
        "auth_key=x", "auth_key=o5xlkgn7my5fmr5c")
    apiURL = re.sub(r"start=\d+", "start=" + str(start), apiURL)
    apiURL = re.sub(r"/user_agent=(.+?)&/", "", apiURL)
    apiURL = re.sub(r"/user_ip=(.+?)&/", "", apiURL)
    apiURL = re.sub(r"/ref_url=(.+?)&/", "", apiURL)
    apiURL = re.sub(r"rows=\d+", "rows=5000", apiURL)
    res = requests.get(apiURL)
    res = json.loads(res.text)
    for i in range(len(res['response']['docs'])):
        currentSku = res['response']['docs'][i]['pid']
        # this splits up color variants into a normal sku
        if currentSku.find('cv') > 0:
            currentSku = currentSku.split('cv')[0]
        pdps.append(currentSku)
    totalPages = math.ceil(res['response']['numFound'] / 5000)
    if totalPages == 0:
        totalPages = 1
    pdps = list(dict.fromkeys(pdps))
    return_data = {
        "data": {
            "totalPages": totalPages,
            "currentPage": page,
            "skus": pdps
        }
    }
    return_data = json.dumps(return_data)
    return(return_data)
