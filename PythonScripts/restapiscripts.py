import requests
import json
import os

AUTH_ENDPOINT1 = "http://127.0.0.1:8000/api/accounts/auth/"
AUTH_ENDPOINT = "http://127.0.0.1:8000/api/accounts/auth/jwt/"
REFRESHAUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/jwt/refresh/"
ENDPOINT = "http://127.0.0.1:8000/api/status/"
image_path = os.path.join(os.getcwd(), 'Screenshot(86).png')



post_headers = {
    "Content-Type": "application/json"
}
auth_data = {
"username": "admin",
"password": "#welcome123"
}

post_method   = requests.post(AUTH_ENDPOINT1, data=json.dumps(auth_data), headers=post_headers)
access_token = post_method.json()
print(post_method.json())

'''
post_headers = {
    # "Content-Type": "application/json",
    "Authorization": "Bearer "+access_token,
}
if image_path is not None:
    with open(image_path, 'rb') as image:
        file_data = {
            'image': image
        }
        data = {
            "content": "new Content-Type NEW 1"
        }
        post_data = json.dumps(data)
        post_response = requests.post(ENDPOINT, data=data, headers=post_headers, files=file_data) # , files=file_data
        # post_response = requests.put(ENDPOINT+str("24"), data=data, headers=post_headers, files=file_data)  # , files=file_data
        # r = requests.request(method, ENDPOINT, data=data, files=file_data, headers=headers)
        print(post_response.text)
else:
    data = {
        "content": "new Content-Type NEW 1"
    }
    post_data = json.dumps(data)
    post_response = requests.post(ENDPOINT, data=data, headers=post_headers) # , files=file_data


'''
# get_endpoint = ENDPOINT + str(12)
# post_data = json.dumps({"content": "Some random content"})
#
# r = requests.get(get_endpoint)
# print(r.text)
#



# r2 = requests.get(ENDPOINT)
# print(r2.status_code)
#
# post_headers = {
#     'content-type': 'application/json'
# }
#
# post_method   = requests.post(ENDPOINT, data=json.dumps(post_data), headers=post_headers)
# print(post_method.text)




''' Below code are Currently not Used '''
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
# do_img(method='put', data={'id':9,'user':1, 'content': "Somthin Good is Yest To come"}, is_json=False, image_path=image_path)

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
