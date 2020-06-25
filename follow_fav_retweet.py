import tweepy
import logging
from bots.configtweepy import set_api
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
            # If this tweet is  reply and it's mine, skip tweet
            return
        if not tweet.favorited:
            # If it is not Liked, Like it.
            try:
                logger.info(f"Add favorite {tweet.id}")

                tweet.favorite()
                time.sleep(1 * 30)

            except Exception as e:
                logger.error("Error on favorite", exc_info=True)
        if not tweet.retweeted:
            # If it is not retweeted. Retweet it.
            try:
                logger.info(f"Retweeting  {tweet.id}")

                tweet.retweet()
                time.sleep(1 * 30)

            except Exception as e:
                logger.error("Error on retweet", exc_info=True)

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
    api = set_api()
    listener = Listener(api)
    stream = tweepy.Stream(api.auth, listener)
    stream.filter(track=keywords, languages=["tr"])

if __name__ == "__main__":
    main(["FatihTerzioglu AcilTahliye"])
    #find "FatihTerzioglu AcilTahliye" tags. Checked and processed them.
