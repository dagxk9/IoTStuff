#!/usr/bin/env python
import sys
from twython import Twython

tweetStr = "test_tweet"
# your twitter consumer and access information goes here
# note: these are garbage strings and won't work
apiKey = 'APIKEYHERE'
apiSecret = 'APISECRETHERE'
accessToken = 'ACCESSTOKENHERE'
accessTokenSecret = 'ACCESSTOKENSECRET'

api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)

api.update_status(status=tweetStr)

print "Tweeted: " + tweetStr