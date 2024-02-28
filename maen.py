import json , requests


def sed_data(data):
    url='http://127.0.0.1:8000/api/add/'
    r=requests.post(url ,json=data)
    return r.status_code

with open('db.json'  , 'r') as file:

    data=json.load(file)

appe=data['Apple']



for i,v in appe.items():
    item = {
        "price":v["price"],
        "img_url":v["img_url"],
        "color":v["color"],
        "ram": v["RAM"],
        "memory":v["memory"],
        "name":v["name"],
        "model":v["company"]
    }
    print(sed_data(item))