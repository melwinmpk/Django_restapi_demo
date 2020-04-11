import json
import requests


BASE_URL = "http://127.0.0.1:8000/"
ENDPOINT = "api/upadtes/"

def get_list():
    r = requests.get(BASE_URL + ENDPOINT)
    print(r.status_code)
    data = r.json()
    print(data)

    for obj in data:
        if obj['id'] == 1:
            r = requests.get(BASE_URL+ENDPOINT+ str(obj['id']))
            print (r.json() )
    return data

def create_update():
    new_data = {
        'user': 1,
        "content": "Some more cool content update"
    }
    r = requests.post(BASE_URL + ENDPOINT, data = json.dumps(new_data)) # json.dumps(new_data)
    print(r.headers)
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        # print(r.json())
        return r.json()
    return r.text

# get_list()

# print(create_update())

def do_obj_update():
    new_data = {
        "content": "New obj data Very Good "
    }
    print(BASE_URL + ENDPOINT + "1/")
    r = requests.put(BASE_URL + ENDPOINT +"1", data=json.dumps(new_data)) # json.dumps(new_data)


    # new_data = {
    #     'id': 1,
    #     "content": "Another new cool update"
    # }
    # r = requests.put(BASE_URL + ENDPOINT, data=new_data)
    # print(r.headers)
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        # print(r.json())
        return r.json()
    return r.text

# print(do_obj_update())

def do_obj_delete():
    new_data = {
        "content": "New obj data "
    }
    print(BASE_URL + ENDPOINT + "12/")
    r = requests.delete(BASE_URL + ENDPOINT +"6")


    # new_data = {
    #     'id': 1,
    #     "content": "Another new cool update"
    # }
    # r = requests.put(BASE_URL + ENDPOINT, data=new_data)
    # print(r.headers)
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        # print(r.json())
        return r.json()
    return r.text

print(do_obj_delete())