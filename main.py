import requests
import json
import pprint
import tweepy
import datetime
import mongoengine
import textblob
import sklearn

from mongoengine import connect
from models import Tweet, Article
from textblob import TextBlob
from similar import cosine_sim

def news():
	r = requests.get(url)

	new_dict = json.loads(r.text)
	pp = pprint.PrettyPrinter(indent=4)

	for item in new_dict['sources']:
		for k, v in item.items():
			if k == "id":
				url2 = "https://newsapi.org/v1/articles?source={0}&apiKey={1}".format(v, key)

				respons = requests.get(url2)
				respons_dict = json.loads(respons.text)

				name_of_source = v

				for item2 in respons_dict['articles']:
					for k,v in item2.items():
						if k == "description":G
							if v is None:
								pass
							elif any(x in v for x in list_words) or all(x in v for x in list_words):
								similarity = cosine_sim(text, item2['description'])
								# if similarity >= 0.2:
								# 	print (similarity, item2['description'])
								dict_to_pass = {
								"source": name_of_source,
								"title": item2["title"],
								"publishedAt": item2["publishedAt"],
								"description": item2["description"]
								}

								article_obj = Article(dict_to_pass)
								article_obj.save()


# user analysis


class StdOutListener(tweepy.StreamListener):

    def on_status(self, status):
        if hasattr (status, 'retweeted_status'):
        	return

        similarity = cosine_sim(text, status.text)

        # if similarity >= 0.2:
        # 	print (similarity, status.text)

        tweet_test = Tweet(tweet= status.text)
        tweet_test.created_at = status.created_at
        tweet_test.save()

    def on_data

    def on_error(self, status):
        if status == 420:
        	return False
# popularuty, urls
# further filter
# snopes.com
# charts and tables
# friends and followers of author of tweets
# independant people


if __name__ == '__main__':

	list_words = []
	list_sentence = []
	list_nouns = []

	key= "e598d1d8a77a45c28d889513a50fb4af"
	url = "https://newsapi.org/v1/sources?language=en"
	text = "Hilary Clinton lost elections in 2016. Donald Trump won!"
	stopwords = ["the", "in", "a"]

	blob = TextBlob(text)

	list_words = blob.words
	b = blob.sentences
	for i in b:
		list_words.append(str(i))

	c = blob.noun_phrases
	for j in c:
		list_words.append(str(j))

	list_words = [word for word in list_words if word not in stopwords]

	connect(db= 'twitter_data')

	news()

	consumer_key = "pZxa21qIfTXxmX6dVIYzB70fr"
	consumer_secret = "kYSwkSro7QqPm7hiGsIapFNIvhy0S57eiz94trji6wOreICJTS"

	access_token = "798765580224327680-JjzdT6URTsJkClNDrbY5c4m5f5Rv7oP"
	access_token_secret = "PVcz8NnZnLMzdJr1VLavSj8yPV4w24acDnyLtK1xhyxl5"

	l = StdOutListener()
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	stream = tweepy.Stream(auth, l)
	stream.filter(track= list_words)


# Real news spread far
# independant parties


