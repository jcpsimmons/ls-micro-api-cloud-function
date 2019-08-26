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
