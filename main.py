#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Simple Bot to reply to Telegram messages.
This is built on the API wrapper, see echobot2.py to see the same example built
on the telegram.ext bot framework.
This program is dedicated to the public domain under the CC0 license.
"""
import os
import atexit
import logging
import telegram
from telegram.error import NetworkError, Unauthorized
from time import sleep
import configparser


update_id = None

def main():
    """Run the bot."""
    global update_id
    # Telegram Bot Authorization Token
    bot = telegram.Bot(config()['TelegramToken'])

    # get the first pending update_id, this is so we can skip over it in case
    # we get an "Unauthorized" exception.
    try:
        update_id = bot.get_updates()[0].update_id
    except IndexError:
        update_id = None

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    while True:
        try:
            pass
            reply(bot)
        except NetworkError:
            sleep(1)
        except Unauthorized:
            # The user has removed or blocked the bot.
            update_id += 1

def config():
    env = ''
    config = configparser.ConfigParser()
    
    if os.environ['ENV'] is not None:
        env = os.environ['ENV']

    config.read(env + '.ini')

    return config['DEFAULT']

def reply(bot):
    """Echo the message the user sent."""
    global update_id
    # Request updates after the last update_id
    for update in bot.get_updates(offset=update_id, timeout=10):
        update_id = update.update_id + 1

        if update.message:  # your bot can receive updates without messages
            # Reply to the message
            update.message.reply_text(update.message.text)
            send_message(bot, config()['TelegramChanel'], update.message.text)

def send_message(bot, group_id, text):
    bot.send_message(group_id, text)

@atexit.register 
def goodbye(): 
    print("GoodBye...")

if __name__ == '__main__':
    main()