from slacker import Slacker
from slack_bot import config


def test_load_config():
    config.load()


def test_hello_world():
    bot_user_token, _ = config.load()
    slack = Slacker(bot_user_token)

    # Send a message to #general channel
    slack.chat.post_message('#slackbot_test', "I'm alive !")
