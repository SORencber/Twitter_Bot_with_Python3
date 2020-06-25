import tweepy
import logging
from bots.configtweepy import set_api
import time

logging.basicConfig(level=logging.INFO)
log = logging.getLogger()


def follow_users(api):
    log.info("Retrieving and following followers")
    for user in tweepy.Cursor(api.followers).items():
        if not user.following:
            log.info(f"Following {user.name}")
            user.follow()


def main():
    api = set_api()
    while True:
        follow_users(api)
        log.info("Waiting...")
        time.sleep(1*60)


if __name__ == "__main__":
    main()
