# NOT COMPLETED/TESTED YET


api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_count=3, retry_delay=60)

db = client.tweets

raw_tweets = db.raw_tweets
users = db.users


def get_followers(user_id):
    users = []
    page_count = 0
    for i, user in enumerate(tweepy.Cursor(api.followers, id=user_id, count=200).pages()):
        print 'Getting page {} for followers'.format(i)
        users += user
    return users

def get_friends(user_id):
    users = []
    page_count = 0
    for user in tweepy.Cursor(api.friends, id=user_id, count=200).pages():
        page_count += 1
        print 'Getting page {} for friends'.format(page_count)
        users.extend(user)
    return users

def get_followers_ids(user_id):
    ids = []
    page_count = 0
    for page in tweepy.Cursor(api.followers_ids, id=user_id, count=5000).pages():
        page_count += 1
        print 'Getting page {} for followers ids'.format(page_count)
        ids.extend(page)

    return ids

def get_friends_ids(user_id):
    ids = []
    page_count = 0
    for page in tweepy.Cursor(api.friends_ids, id=user_id, count=5000).pages():
        page_count += 1
        print 'Getting page {} for friends ids'.format(page_count)
        ids.extend(page)
    return ids


