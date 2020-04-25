import requests
import json

ENDPOINT = "http://127.0.0.1:8000/api/status/"

def do(method='get', data={}, is_json=True):
    headers = {}
    URL = ENDPOINT # + "?id=" + str(id)
    if is_json:
        headers['content-type'] = 'application/json'
        data = json.dumps(data)
    print("============Debugger================")
    print(URL)
    print("============Debugger================")
    r = requests.request(method, URL, data=data, headers=headers)
    print(r.text)
    print(r.status_code)
    return r

# do(data={'id':8})
# do(method='delete', data={'id':8})
# do(method='put', data={'id':3,'user':1,'content':"some cool new content"})
do(method='put', data={'user':1,'content':"some cool new content"})