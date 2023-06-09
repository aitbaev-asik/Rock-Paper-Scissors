import os
import random
import telebot
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Давай поиграем в камень-ножницы-бумагу.\nВведи /play, чтобы начать игру.")

@bot.message_handler(commands=['play'])
def play_game(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = telebot.types.KeyboardButton('Камень')
    item2 = telebot.types.KeyboardButton('Ножницы')
    item3 = telebot.types.KeyboardButton('Бумага')
    markup.add(item1, item2, item3)
    bot.reply_to(message, "Выбери свой ход:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_choice = message.text.lower()
    bot_choice = random.choice(['камень', 'ножницы', 'бумага'])
    if user_choice in ['камень', 'ножницы', 'бумага']:
        if user_choice == bot_choice:
            result = "Ничья!"
        elif user_choice == 'камень' and bot_choice == 'ножницы' \
            or user_choice == 'ножницы' and bot_choice == 'бумага' \
            or user_choice == 'бумага' and bot_choice == 'камень':
            result = "Ты выиграл!"
        else:
            result = "Ты проиграл :("
        bot.reply_to(message, f"Ты выбрал {user_choice}, а я выбрал {bot_choice}. {result}")
    else:
        bot.reply_to(message, "Не понимаю, что ты имеешь в виду. Выбери камень, ножницы или бумагу.")

if __name__=='__main__':
    print('Bot started')
    bot.polling(non_stop=True)