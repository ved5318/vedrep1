import twitter
from datetime import datetime
from FlaskApp import db
from FlaskApp import consumer_token, consumer_secret
from FlaskApp.models import User

my_id = ''
my_name = ''
my_twitter_handler = ''
api = None

def create_api(access_token, access_token_secret):
    global api, my_id, my_name
    api = twitter.Api(consumer_key=consumer_token,
                    consumer_secret=consumer_secret,
                    access_token_key=access_token,
                    access_token_secret=access_token_secret)
    api.DEFAULT_CACHE_TIMEOUT= 60
    my_credentials = api.VerifyCredentials()
    my_id = my_credentials.id
    my_name = my_credentials.name
    my_twitter_handler = my_credentials.screen_name
    print(f'---------------"{my_twitter_handler}"-------------------')

def get_my_id():
    return my_id

def get_my_twitter_handler():
    return my_twitter_handler

def my_timeline():
    tweets = api.GetHomeTimeline()
    return tweets


def my_tweets():
    tweets = api.GetUserTimeline(my_id)
    return tweets
    
def post_tweet(msg):
    tweet =  api.PostUpdate(msg)
    if(tweet):
        return True
    else:
        return False

def my_friends():
    my_friends = api.GetFriends()
    return my_friends


def getUserName_Pic(twitter_id):
	user = api.GetUser(twitter_id)
	name = user.name
	pic = user.profile_image_url 
	return name, pic
