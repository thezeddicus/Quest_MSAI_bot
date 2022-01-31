import telebot
import config
from telebot import types
from ORM import *
import time

bot = telebot.TeleBot(config.TOKEN) # bot token

# command /reg(register)
@bot.message_handler(commands=['reg'])
def register(message):

	item1 = types.KeyboardButton("Red team")
	item2 = types.KeyboardButton("Blue team")
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(item1, item2)
	bot.send_message(message.chat.id, "Choose your team", reply_markup=markup)
	bot.register_next_step_handler(message, choice)

# content type(text)
@bot.message_handler(content_types="text")
def choice(message):
	item1 = types.KeyboardButton("Ready")
	item2 = types.KeyboardButton("Not ready")

	markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(item1, item2)

	if message.text == "Red team":
		

		bot.send_message(message.chat.id, "You are in the Red team, GLHF", reply_markup=markup)
		bot.register_next_step_handler(message, info)

	elif message.text == "Blue team":

		bot.send_message(message.chat.id, "You are in the Blue team, GLHF", reply_markup=markup)
		bot.register_next_step_handler(message, info)

def info(message):
	if message.text == "Ready":
		global start_time
		start_time = int(time.time())
		markup = types.ReplyKeyboardRemove(selective=True)
		bot.send_message(message.chat.id, "The goal is to find out the sentence that we created")
		bot.send_message(message.chat.id, "You can find first clue here: https://goo.gl/maps/idMSZPHuxj3zmMMKA", reply_markup=markup)
		bot.register_next_step_handler(message, one)

	elif message.text == "Not ready":
		item1 = types.KeyboardButton("Red team")
		item2 = types.KeyboardButton("Blue team")
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(item1, item2)
		bot.send_message(message.chat.id, "Choose your team", reply_markup=markup)
		bot.register_next_step_handler(message, choice)

# word1
def one(message):
	
	if message.text == word1:
		bot.send_message(message.chat.id, "First one is on point, find remaining 4)")
		bot.send_message(message.chat.id, "Second one located here: https://goo.gl/maps/2LyneZMcgn1J6amP9")
		bot.register_next_step_handler(message, two)
		
		
	else:
		bot.send_message(message.chat.id, "Incorrect answer")
		bot.register_next_step_handler(message, one)

# word2
def two(message):
	
	if message.text == word2:
		bot.send_message(message.chat.id, "Second one is on point, find remaining 3)")
		bot.send_message(message.chat.id, "Third one located here: https://goo.gl/maps/RLJVzHp3z4Z2ntK86")
		bot.register_next_step_handler(message, three)
		
	else:
		bot.send_message(message.chat.id, "Incorrect answer")
		bot.register_next_step_handler(message, two)

# word3
def three(message):
	
	if message.text == word3:
		bot.send_message(message.chat.id, "Third one is on point, find remaining 2")
		bot.send_message(message.chat.id, "Fourth one located here: https://goo.gl/maps/g9eJMfSxMVoA3Xis7")
		bot.register_next_step_handler(message, four)
		
	else:
		bot.send_message(message.chat.id, "Incorrect answer")
		bot.register_next_step_handler(message, three)

# word4
def four(message):
	
	if message.text == word4:
		bot.send_message(message.chat.id, "Fourth one is on point, find final clue")
		bot.send_message(message.chat.id, "Final clue located here: https://goo.gl/maps/g9eJMfSxMVoA3Xis7")
		bot.register_next_step_handler(message, five)
		
	else:
		bot.send_message(message.chat.id, "Incorrect answer")
		bot.register_next_step_handler(message, four)

# word5
def five(message):
	
	if message.text == word5:
		finish_time = int(time.time()) - start_time
		bot.send_message(message.chat.id, f"You have completed our quest, Gratz.You spent {finish_time} seconds, Whole sentence: <b>{word1+word2+word3+word4+word5}</b> try again?", parse_mode="html")

		
	else:
		bot.send_message(message.chat.id, "Incorrect answer")
		bot.register_next_step_handler(message, five)



print("Connected")
bot.polling() # Run bot
