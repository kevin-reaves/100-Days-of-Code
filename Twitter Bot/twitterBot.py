#!/usr/bin/python
"""
Thanks to Hiztory.org for the free api
http://www.hiztory.org/
"""

import tweepy, requests
from datetime import datetime
from credentials import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# api.update_status('Hello World! Testing Tweepy setup.')

def requestHistory(date):
    baseURL = "http://api.hiztory.org/"

    curDate = date.split('-')

    #For some reason I thought I needed year
    #year = curDate[0]
    month = curDate[1]
    day = curDate[2]

    url = baseURL + "date/event/" + month + "/" + day + "/api.xml"

    history = requests.get(url, verify=False)
    newHistory = history.text.split("\"")

    print("On " + month + "/" + day + ", " + newHistory[9] + ".")

requestHistory(str(datetime.now().date()))
