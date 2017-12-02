#!/usr/bin/python
"""
Thanks to Hiztory.org for the free api
http://www.hiztory.org/
"""

import tweepy, requests, re
from datetime import datetime, timedelta
from time import sleep
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

    #Version using split and indexing, moving to RE
    #newHistory = history.text.split("\"")
    #print("On " + month + "/" + day + ", " + newHistory[9] + ".")

    code200Regex = re.search(r'.*status code="(\d{3})"', history.text)

    if code200Regex.group(1) == '200':
        try:
            contentRegex = re.search(r'.*content="(.*)"', history.text)

            newHistory = "On " + month + "/" + day + ", " + \
                         contentRegex.group(1) + "."

            api.update_status(newHistory + "\nCredit http://www.hiztory.org/")
        except tweepy.error.TweepError:
            #In case this is run more than once a day
            pass
    else:
        api.update_status("@kevin82593 " + code200Regex.group(1))



def likeTweets():
    sinceDate = datetime.now() - timedelta(days=2)
    sinceDate = sinceDate.date()

    for tweet in tweepy.Cursor(api.search, q="#100DaysOfCode",
                               since=sinceDate).items():
        try:
            #Hits rate limit without sleeping
            sleep(5)
            if not tweet.favorited:
                api.create_favorite(tweet.id)
        #From what I can tell, Twitter's api may not always catch this
        #We can ignore the error
        except Exception as e:
            print(e)

requestHistory(str(datetime.now().date()))
likeTweets()