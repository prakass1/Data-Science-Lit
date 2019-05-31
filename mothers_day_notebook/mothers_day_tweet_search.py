import pandas as pd
import json
import requests as rq
from requests_oauthlib import OAuth1
import datetime
import time

url = "https://api.twitter.com/1.1/search/tweets.json"

keywords = ["Happy Mother" ,"mom is best", "mothers day love", "moms love", "amazing moms"]


'''
$ curl --request GET 
 --url 'https://api.twitter.com/1.1/search/tweets.json?q=nasa&result_type=popular' 
 --header 'authorization: OAuth oauth_consumer_key="consumer-key-for-app", 
 oauth_nonce="generated-nonce", oauth_signature="generated-signature", 
 oauth_signature_method="HMAC-SHA1", oauth_timestamp="generated-timestamp", 
 oauth_token="access-token-for-authed-user", oauth_version="1.0"'


headers={'authorization': 'OAuth',
             'oauth_consumer_key':"mNCkklH3qGaoWzmUBy16im9fu",
             'oauth_nonce':'generated-nonce',
             'oauth_signature':'generated-signature',
             'oauth_signature_method':'HMAC-SHA1',
             'oauth_timestamp':'generated-timestamp',
             'oauth_token':'3038733591-kyqdatnReOb8d1PHOs2nBIO93sIlGEyv5iq9CO5',
             'oauth_version':'1.0'
             }
 
'''

#API access
API_KEY = "XXXXXX_XXXXXXXXX_XXXXXXXXXX"
API_SECRET = "XXXXXX_XXXXXXXXX_XXXXXXXXXX" 
ACCESS_TOKEN = "XXXXXX_XXXXXXXXX_XXXXXXXXXX"
ACCESS_TOKEN_SECRET = "XXXXXX_XXXXXXXXX_XXXXXXXXXX"

#OAuth1
auth = OAuth1(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

#Make a request to api.twitter.com/search
def make_req(keywords):
    for keyword in keywords:
        response = rq.get(
    url,auth=auth, params={'q': keyword,
                           "lang": "en",
                           "result_type":"mixed",
                           "count":100} )
    #params={'q': 'requests+language:python'})
        if response.status_code != 200:
            continue
        with open("json_dumps//"+str("".join(keyword.strip()))+".json", 'w+') as outfile:
                  json.dump(response.json(), outfile, indent=4)
                  outfile.close()
		#Sleep for 15min
        time.sleep(960)

#For 10 requests create respective jsons
make_req(keywords)
