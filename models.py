import mongoengine
import datetime

from mongoengine import *

class Tweet(Document):
	status = StringField()
	created_at = DateTimeField(default=datetime.datetime.now)
	user = StringField()
	user_id = StringField()
	followers = IntField()
	friends = IntField()
	verified = BooleanField()
	geo = StringField()
	ip = StringField()
	similarity = DecimalField()

class Article(Document):
	source = DynamicField()
	title = StringField()
	description = StringField()
	publishedAt = DateTimeField(default= datetime.datetime.now)
	similarity = DecimalField()
