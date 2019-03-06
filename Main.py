from TwitterAPI import TwitterAPI
from threader import Threader
import guizero
# from twython import Twython
import math
# import time
from textwrap import wrap
from apikeys import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)


source_selected = True

keys = dict(consumer_key=consumer_key,
            consumer_secret=consumer_secret,
            access_token_key=access_token,
            access_token_secret=access_token_secret)
api = TwitterAPI(**keys)


def send_tweet():
    print("send tweet")
    tweet_array = wrap(tweet.value, 240)
    th = Threader(tweet_array, api, wait=slider.value)
    th.send_tweets()

#
# def insert_selected():
#     api_key_line.show()
#     choose_key_area.hide()
#     global source_selected
#     source_selected = True
#
#
# def import_selected():
#     import_key_area.show()
#     choose_key_area.hide()
#     global source_selected
#     source_selected = True


def submit_validation():
    send_tweet()


def count():
    pass
# number_of_chars.value = "Number of Chars: " + str(len(tweet.value) - 1)


def count_tweets():
    num = (math.ceil((len(tweet.value) - 1)/250))
    number_of_tweets.value = "Number of Tweets: " + str(num)


if __name__ == '__main__':
    app = guizero.App()
    title_box = guizero.Box(app, align='top')

# title box
    title = guizero.Text(title_box, "Send a Tweet!", align='top')

# # read from file or show key
#     choose_key_area = guizero.Box(app, visible=True)
#     choose_insert_key = guizero.PushButton(choose_key_area, text="Insert Key", align="left", command=insert_selected)
#     choose_import_key = guizero.PushButton(choose_key_area, text="Import Key", align="right", command=import_selected)
#

# # one line: insert key, button
#     api_key_line = guizero.Box(title_box, visible=False)
#
#     list_of_keys_area = guizero.Box(title_box, visible=False,)
#
#     consumer_key = guizero.TextBox(list_of_keys_area, "consumer_key", width=60)
#     consumer_secret = guizero.TextBox(list_of_keys_area, "consumer_secret", width=60)
#     access_token = guizero.TextBox(list_of_keys_area, "access_token", width=60)
#     access_token_secret = guizero.TextBox(list_of_keys_area, "access_token_secret", width=60)
#
#     insert_key = guizero.PushButton(api_key_line, text="submit key", align="right")
#
#     # one line: read from file
#     import_key_area = guizero.Box(app, visible=False)
#     api_key = guizero.TextBox(import_key_area, "./apikey.txt", width=60, align="left")
#     import_button = guizero.PushButton(import_key_area, text="Import", align="right")


# tweet composition box
    tweet_composition_area = guizero.Box(app)
    tweet = guizero.TextBox(tweet_composition_area, text="Compose Tweet Here", height=15, width='fill', multiline=True)
    tweet.when_key_released = count

# stats area
    stats_area = guizero.Box(app)


# num of tweets line
    number_of_tweets = guizero.Text(stats_area, text="Number of Tweets: 1")
    tweet.when_key_released = count_tweets

# wait time slider
    wait_time_area = guizero.Box(stats_area)
    wait_time_text = guizero.Text(wait_time_area, text="Seconds Between tweets:", align="left")
    slider = guizero.Slider(wait_time_area, start=180, end=1, align="right", horizontal=False)


# submit area
    submit_area = guizero.Box(app)
    submit = guizero.PushButton(submit_area, text="Submit!", command=submit_validation)
    app.display()
    # send_tweet()
