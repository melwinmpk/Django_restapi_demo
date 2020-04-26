import requests
import json
import os

ENDPOINT = "http://127.0.0.1:8000/api/status/"
image_path = os.path.join(os.getcwd(), 'Screenshot(86).png')

def do_img(method='get', data={}, is_json=True, image_path=None):
    headers = {}
    URL = ENDPOINT # + "?id=" + str(id)
    if is_json:
        headers['content-type'] = 'application/json'
        data = json.dumps(data)
    if image_path is not None:
        with open(image_path, 'rb') as image:
            file_data = {
                'image': image
            }
            r = requests.request(method, ENDPOINT, data=data, files=file_data, headers=headers)
    else:
        r = requests.request(method, URL, data=data, headers=headers)
    print(r.text)
    print(r.status_code)
    return r

# do_img(method='post', data={'user':1, 'content': ""}, is_json=False, image_path=image_path)
do_img(method='put', data={'id':9,'user':1, 'content': "Somthin Good is Yest To come"}, is_json=False, image_path=image_path)

def do(method='get', data={}, is_json=True):
    headers = {}
    URL = ENDPOINT # + "?id=" + str(id)
    if is_json:
        headers['content-type'] = 'application/json'
        data = json.dumps(data)
    r = requests.request(method, URL, data=data, headers=headers)
    print(r.text)
    print(r.status_code)
    return r


# print("============Debugger================")
    # print(URL)
    # print("============Debugger================")
# do(data={'id':8})
# do(method='delete', data={'id':8})
# do(method='put', data={'id':3,'user':1,'content':"some cool new content"})
# do(method='put', data={'user':1,'content':"some cool new content"})
