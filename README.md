# ls-micro-api-cloud-function
Micro-API for retrieving product data from Firebase. Each folder deploys on a Google Cloud Function. All functions should have "Content-Type" set to "application/json".

---

## getSkuData

**POST** request. Send a SKU, get all associated product data. Request JSON should be formatted as follows:
```
{
    "sku": "246776"
}
```
or multiple SKUs
```
{
    "sku": "246776,100045,241982"
}
```

---

## bloomreachSkusonPlp

**ENDPOINT:** https://us-central1-root-catfish-206221.cloudfunctions.net/bloomreach-skus-on-plps 

**POST** request. Send PLP URL and page for request, and get back SKUs (up to 5000) that are on the PLP. Request JSON formatting as follows:
```
{
    "url": "https://www.livingspaces.com/departments/rugs/type/area-rugs",
    "page": 1
}
```
**SAMPLE RESPONSE** SKUs truncated for documentation purposes
```
{
    "data": 
    {
        "totalPages": 2, 
        "currentPage": 1, 
        "skus": ["108064", "110488", "237178", "110487", "110483", "237162", "108374", "94830", "245009"]
    }
}
```