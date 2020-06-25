import tweepy
import logging

log = logging.getLogger()

def set_api():
    consumer_key = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    consumer_secret = 'XXXXXXXXXXXXXXXX'
    access_token = 'XXXXXXXXXXXXXXXXXXX-XXXXXX'
    access_token_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXX'
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        log.error("Error creating API", exc_info=True)
        raise e
    log.info("API created")
    return api

