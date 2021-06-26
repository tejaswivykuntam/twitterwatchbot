import tweepy
import src.credentials as cred

follow = ['833112575881641984'] # Insert id here. id can be obtained from https://tweeterid.com/
track = ['Resident Evil Village', 'Cyberpunk 2077'] # Insert keywords to track here.
class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()
        
    def on_status(self, tweet):
        print (f"{tweet.user.name}:{tweet.text}")
        
    def on_error(self, status):
        print("Error detected")

# Authenticate to twitter
auth =  tweepy.OAuthHandler(cred.CONSUMER_KEY, cred.CONSUMER_SECRET)
auth.set_access_token(cred.ACCESS_TOKEN, cred.ACCESS_TOKEN_SECRET)
# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
tweets_listener = MyStreamListener(api)
stream = tweepy.Stream(api.auth, tweets_listener)
stream.filter(follow = follow, track = track)
