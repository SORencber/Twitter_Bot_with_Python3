import tweepy
import logging
from bots.configtweepy import create_api
import json
import time
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

class Listener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_limit(self, status):
        print("Rate Limit Exceeded, Sleep for 15 Mins")
        time.sleep(6 * 60)
        return True

    def on_status(self, tweet):
        logger.info(f"Processing tweet id {tweet.id}")
        if tweet.in_reply_to_status_id is not None or \
            tweet.user.id == self.me.id:
            # This tweet is a reply or I'm its author so, ignore it
            return
        if not tweet.favorited:
            # Mark it as Liked, since we have not done it yet
            try:
                logger.info(f"Add favorite tweet id {tweet.id}")

                tweet.favorite()
                time.sleep(1 * 30)

            except Exception as e:
                logger.error("Error on fav", exc_info=True)
        if not tweet.retweeted:
            # Retweet, since we have not retweeted it yet
            try:
                logger.info(f"Retweeting tweet id {tweet.id}")

                tweet.retweet()
                time.sleep(1 * 30)

            except Exception as e:
                logger.error("Error on fav and retweet", exc_info=True)

        if not tweet.user.following:
            try:
                logger.info(f"Following  tweet user {tweet.user}")

                tweet.user.follow()
                time.sleep(1 * 30)

            except Exception as e:
                logger.error("Error on following", exc_info=True)
    def on_error(self, status):
        logger.error(status)

def main(keywords):
    api = create_api()
    tweets_listener = Listener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=keywords, languages=["tr"])

if __name__ == "__main__":
    main(["FatihTerzioglu AcilTahliye"])
