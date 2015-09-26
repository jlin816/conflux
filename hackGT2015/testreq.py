import requests
# import requests_oauthlib
import json
# access_token= '7a0e8190e2f42cf03dfd04b0cd7cd355ea5490d8'
headers = {"Authorization":"Token f281c414269bba6954b1a9b55188e0b54b0afd08"}
payload = {'plaid_token':'test_wells'}
print payload
print requests.post('http://localhost:8000/api/user/', headers = headers).text
# print requests.post('http://localhost:8000/api/forceUpdatePlaid/', headers = headers).text
