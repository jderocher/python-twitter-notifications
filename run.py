#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API

from settings import access_token
from settings import access_token_secret
from settings import consumer_key
from settings import consumer_secret
from settings import qt_source_string


class StdOutListener(StreamListener):



    def on_status(self, status):
        screen_name = status.user.screen_name


        if hasattr(status, 'quoted_status'):
            quote_tweet = status.quoted_status._json
            if 'user' in quote_tweet:
                if quote_tweet['user'] is not None:
                    if "screen_name" in quote_tweet['user']:
                        if quote_tweet['user']['screen_name'] is not None:

                            # Filter by username
                            quote_tweet_screen_name = quote_tweet['user']['screen_name']
                            if quote_tweet['user']['screen_name'].lower() is qt_source_string:
                                if quote_tweet['user']['url'] is not None:
                                    #og_quote_url = "https://twitter.com/" + str(quote_tweet['user']['id']) + "/status/" + str(quote_tweet['id'])
                                    quote_url = "https://twitter.com/" + str(status._json['user']['id']) + "/status/" + str(status._json['id'])
                                    if status._json['text'] is not None:
                                        #og_quote_text = quote_tweet['text']
                                        quote_text = status._json['text']
                                        qts += 1
                                        print(screen_name + " quote tweeted " + quote_tweet_screen_name + " at " + quote_url + " saying: " + quote_text)

        return True



if __name__ == '__main__':
    l = StdOutListener()

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    auth_api = API(auth)
    print("Account Auth: "+auth_api.me().name)
    print("Preparing stream ...")

    stream = Stream(auth, l, timeout=20)
    #searches = ['trump']
    stream.sample()
