import requests,pprint
from datetime import date,timedelta
# import requests_oauthlib
pp = pprint.PrettyPrinter(indent=4)
BASE_URL = 'https://tartan.plaid.com'
client_id = '54bdbbb5d6c6ee9c0a5d42a3'
secret = '5a8bb00f6b94d0b04a7f6e3443bdad'
access_token = 'test_wells'
payload = {'client_id':client_id, 'secret':secret, 'access_token':access_token, 'gte': (date.today()-timedelta(days=-1)).isoformat()}
r=requests.post(BASE_URL + '/connect/get',json=payload).json()
pp.pprint(r)
# print requests.get('http://127.0.0.1:8000/api/user/',headers={"Authorization": "Token ffc5e918f8a69c4d0056612c982762a8d5c36e58"}).json()