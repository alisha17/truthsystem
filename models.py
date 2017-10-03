import mongoengine
import datetime

from mongoengine import *

class Tweet(Document):
	tweet = StringField(max_length=200)
	date = DateTimeField(default=datetime.datetime.now)
	similarity = DecimalField()

class Article(Document):
	source = DynamicField()
	title = StringField()
	description = StringField()
	publishedAt = DateTimeField(default= datetime.datetime.now)
	similarity = DecimalField()
