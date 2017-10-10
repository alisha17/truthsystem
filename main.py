import requests
import json
import pprint
import tweepy
import datetime
import mongoengine
import textblob
import sklearn
from collections import Counter

from mongoengine import connect
from models import Tweet, Article
from textblob import TextBlob
from similar import cosine_sim

# TO DO:
# make this work
# store in the table
# write function to check link from one user to another user

def news():
	"""
      Fetch news articles and save them, for now leave this
	"""
	r = requests.get(url)

	new_dict = json.loads(r.text)

	pp = pprint.PrettyPrinter(indent=4)

	for item in new_dict['sources']:
		newsSource = item['id']
		newsApiData = "https://newsapi.org/v1/articles?source={0}&apiKey={1}".format(newsSource, key)
		respons = requests.get(newsApiData)
		response_dict = json.loads(respons.text)
		# print (response_dict)
		name_of_source = newsSource
		for article in response_dict['articles']:
			description = article['description']
			if(description==None):
				break

			wordFrequency=Counter()
			for x in description.split(' '):
				wordFrequency[x] += 1
			if any(wordFrequency.get(x)!=None for x in list_words) or all(wordFrequency.get(x)!=None for x in list_words):
				similarity = cosine_sim(text, description)
				print (similarity)
				# if similarity >= 0.2:
				# 	print (similarity, item2['description'])
				dict_to_pass = {
				"source": name_of_source,
				"title": article["title"],
				"publishedAt": article["publishedAt"],
				"description": article["description"]
				}

				article_obj = Article(dict_to_pass)
				article_obj.save()


class StdOutListener(tweepy.StreamListener):
	"""
       Tweepy class for streaming data
	"""

	def __init__(self, api=None):
		super(StdOutListener, self).__init__()
		self.num_tweets = 0

	def on_status(self, status):
		if hasattr (status, 'retweeted_status'):
			return

		self.num_tweets += 1

		if self.num_tweets < 20:
			if cosine_sim(text, status.text) != 0.0:
				status1 = status.text.lower()
				tweet_test = Tweet(status = status1)
				tweet_test.created_at = status.created_at
				tweet_test.user = status.user.screen_name
				tweet_test.user_id = status.user.id_str
				tweet_test.followers = status.user.followers_count
				tweet_test.friends = status.user.friends_count
				tweet_test.verified = status.user.verified
				tweet_test.similarity = cosine_sim(text, status.text)
				tweet_test.save()
				print (self.num_tweets)
				return True
		else:
			return False


	def on_error(self, status):
		if status == 420:
			return False

# 19773456
# 19773464

# charts and tables

if __name__ == '__main__':

	list_words = []
	list_sentence = []
	list_nouns = []
	count = 0

	key= "XXXXXXXXXXXXXXXXX"
	url = "https://newsapi.org/v1/sources?language=en"
	text = "Ivana Trump I am first lady".lower()
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

	connect(db = 'twitter_data')

	# news()

	consumer_key = "XXXXXXXXX"
	consumer_secret = "XXXXXXX"

	access_token = "XXXXXXXXX"
	access_token_secret = "XXXXXX"

	l = StdOutListener()
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	stream = tweepy.Stream(auth, l)
	stream.filter(track= list_words)

	Tweet.objects.order_by('-created_at')
	print ("I am done")

	# for document in Tweet.objects:




# Real news spread far
# independant parties


