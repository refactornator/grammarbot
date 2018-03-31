import os
import http.client, urllib.parse, json

host = 'api.cognitive.microsoft.com'
path = '/bing/v7.0/spellcheck'

def spellcheck(text):
    key = os.environ['BING_KEY']
    params = {'mkt': 'en-US', 'mode': 'proof', 'text': text}

    headers = {'Ocp-Apim-Subscription-Key': key,
    'Content-Type': 'application/x-www-form-urlencoded'}

    conn = http.client.HTTPSConnection(host)
    params = urllib.parse.urlencode(params)
    conn.request("POST", path, params, headers)
    response = conn.getresponse()
    return response.read()
