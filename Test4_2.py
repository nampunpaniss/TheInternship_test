import json 
from typing import Optional
from Test4_1 import getCompanies
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/companies")
def get_companies():
    json_data = {"companies" : []}
    data = getCompanies()
    for x in data :
        json_data['companies'].append({'logo' : x['img']})
    return json.dumps(json_data)