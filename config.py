import tweepy

#Consumer and Access code for twitter api
consumer_key = "XXXXXXXXXX"
consumer_secret = "XXXXXXXXXX"

access_token = "XXXXXXXXXX"
access_token_secret = "XXXXXXXXXX"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#News Api key
key= "XXXXXXXXXX"