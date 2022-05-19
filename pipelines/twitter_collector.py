from msilib.sequence import tables
import tweepy
import pandas as pd
from urllib.parse import quote as url_quote
from helpers.sentiment_analyzer_modules import get_sentiment_result
import requests
sentiment_threshold = 0.1


class TwitterGatherer(object):
    def __init__(self):
        self.auth = tweepy.OAuthHandler("oUMiWdZe7mGlGa5WDe3lbPyeb", "e5sNqVu67TeQAN5xRo57a3hSymxzV0J2QYR6RDZCAeOGfKL5fo")
        self.auth.set_access_token("854550216611160064-mfrwblzzpPqIJDXyVz850ubyBXYCKYa", "HNLdbjg2AT69Ug75KMFQ820Ud5IKeKJZoFTD9tuFuWtFG")
        self.auth.secure = False
        self.api_client = tweepy.API(self.auth)
        self.usable_columns = ["username", "description_of_user", 
        "location", "following", "followers", "total_tweets", "retweeted_count", 
        "hashtags","text"]

    def getTweets(self, keywords, tweets_from, batch_size):
        
        dataframe = pd.DataFrame(columns = self.usable_columns)
        search_query = url_quote(keywords)
        tweet_gen_obj = tweepy.Cursor(self.api_client.search_tweets,
                               keywords, 
                               lang="en",
                               since_id=tweets_from,
                               tweet_mode='extended').items(batch_size)
        for tweet in tweet_gen_obj:
            print(tweet)
            username = tweet.user.screen_name  # can have an improvement to have verified accounts a greater weightage in future.
            description = tweet.user.description # same as above.
            location = tweet.user.location # can have analysis in the future on sentiments of people of each region.
            following = tweet.user.friends_count # Ratio of following and follwers impacts the credibility of the account greatly.
            followers = tweet.user.followers_count
            totaltweets = tweet.user.statuses_count # can be used in the future for weighted scoring to avoid repeat notifications by the same user.
            retweetcount = tweet.retweet_count # might not be relevant for this use case as we are collecting the retweeted tweet as well, but keeping it for future reference.
            hashtags = tweet.entities['hashtags'] # Collecting hashtags , to allow for future searches.
            try:
                text = tweet.retweeted_status.full_text
            except AttributeError:
                text = tweet.full_text
            
            insertion_dict = dict(
                zip(self.usable_columns, 
                [username, description, location, following, followers, totaltweets, retweetcount, hashtags, text]
                )
                )
            dataframe.append(insertion_dict, ignore_index = True)
        return dataframe
            






 