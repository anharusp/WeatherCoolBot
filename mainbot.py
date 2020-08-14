import telebot
import time
import datetime
import requests
import os

import config
from weather_api import forecast_location, forecast_manual

#config vars
token = os.environ['TELEGRAM_TOKEN']

bot = telebot.TeleBot(token)
city_name = 'Moscow'

keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Enter location', telebot.types.KeyboardButton('Send location', request_location=True))

@bot.message_handler(commands=['start', 'help'])
def start_message(message):
    bot.send_message(message.chat.id, config.START_MSG, reply_markup=keyboard1)

@bot.message_handler(commands=['stop'])
def stop_message(message):
    bot.send_message(message.chat.id, "Thank you for using WeatherCoolBoot!")
    bot.register_next_step_handler(message, send_text)

@bot.message_handler(content_types=["location"])
def location(message):
    if message.location is not None:
        print(message.location)
        print("latitude: %s; longitude: %s" % (message.location.latitude, message.location.longitude))
        bot.send_location(message.chat.id, message.location.latitude, message.location.longitude)
        msg, sticker_id = forecast_location(message.location.latitude, message.location.longitude)
        bot.send_message(message.chat.id, msg)
        bot.send_sticker(message.chat.id, sticker_id)
        bot.send_message(message.chat.id, "If you want to choose other location - click on the necessary button", reply_markup=keyboard1)

def user_entering_city(message):
    if message.text == 'Enter location':
        bot.send_message(message.chat.id, 'Enter your city')
        bot.register_next_step_handler(message, user_entering_city)
    elif message.text == "Send location":
        bot.send_message(message.chat.id, 'Here is your location')
    else:
        city_name = message.text
        msg, sticker_id = forecast_manual(city_name)
        bot.send_message(message.chat.id, msg)
        bot.send_sticker(message.chat.id, sticker_id)
        if (msg==config.sorry_msg):
            bot.register_next_step_handler(message, user_entering_city)
        else:
            bot.send_message(message.chat.id, "If you want to choose other location - click on the necessary button", reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def send_text(message):
    print('The message was recieved: ', message.text)
    if message.text == 'Enter location':
        bot.send_message(message.chat.id, 'Enter your city')
        bot.register_next_step_handler(message, user_entering_city)
    elif message.text == "Send location":
        bot.send_message(message.chat.id, 'Here is your location')
    else:
        print(message.chat.id)
        bot.send_message(message.chat.id, 'What do you mean?')

@bot.message_handler(content_types=['sticker'])
def send_sticker(message):
    #print('The message was recieved: ', message.text)
    print('Sticker recieved', message.sticker.file_id)


if __name__ == '__main__':
    try:
        bot.polling(none_stop=True)
    except:
        pass


