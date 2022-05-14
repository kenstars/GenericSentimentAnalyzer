"""
 PROBLEM STATEMENT
 
 There is a lot of news coverage and social media discussion on the situation in Ukraine. 
 A client has asked you to work with a proof of concept to build a solution to collect 
 and analyze sentiment related to Ukraine from different sources in 1 platform. Eventually, 
 they would like to use this platform to analyze data for other topics beyond Ukraine, 
 but feel that 1 case (Ukraine) and 1 data source will make a good scope for the POC. 
 Write code for collection and processing for the first source so that it can be presented 
 in an upcoming meeting with the client.

"""
from time import time
import json
from pipelines.twitter_collector import TwitterGatherer

if __name__ == "__main__":
    twitter_obj = TwitterGatherer()
    with open("config/collection_config.json") as r:
        config = json.load(r)
    tweets_from = config["tweets_from"]
    keywords = config["keywords"]
    batch_size = config["batch_size"]
    tweet_df = twitter_obj.getTweets(keywords, tweets_from, batch_size)
    epoch_now = str(time())
    tweet_df.to_csv(f"data/tweets_until_{epoch_now}.csv", index = False)
