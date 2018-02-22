import requests
import json
import time

#url = 'https://api.bitso.com/v3/ticker/'
url = 'https://api.bitso.com/v3/order_book?book=btc_mxn'
response = requests.get(url)
#print (response)
ad = json.loads(response.text)
#print (ad['payload']['bids'][0])
#print (ad['payload']['asks'][0])
Var = ad['payload']['asks'][0]['price']
print (Var)
time.sleep(5)
response = requests.get(url)
ad = json.loads(response.text)
Bar = ad['payload']['bids'][0]['price']
print (Bar)
print ('Evaluación:', float(Bar)/float(Var))

