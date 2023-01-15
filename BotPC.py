import random
import pyscreenshot
import os
import telebot
from telebot import types 

frase = ('Мой список команд:\n /Anime /Youtube /help /start привет!')
chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFHGIJKLNOPQRSTUVWXYZ'
bot = telebot.TeleBot('ENTER TOKEN PLEASE')

@bot.message_handler(commands=['Youtube'])
def website(message):
      markup = types.InlineKeyboardMarkup()
      button1 = types.InlineKeyboardButton("Ютубчик!", url='https://www.youtube.com/')
      markup.add(button1)
      bot.send_message(message.chat.id, "Привет, {0.first_name}! Нажми на кнопку и перейди на сайт)".format(message.from_user), reply_markup=markup)
@bot.message_handler(commands=['Anime'])
def website(message):
      markup = types.InlineKeyboardMarkup()
      button2 = types.InlineKeyboardButton("Аниме сайтик!!", url='https://animego.org/anime')
      markup.add(button2)
      bot.send_message(message.chat.id, "Привет {0.first_name}! Нажми на кнопку и перейди на сайт)".format(message.from_user), reply_markup=markup)
@bot.message_handler(commands=['help'] )
def website(message):
      if (message.text == '/help'):
        bot.send_message(message.chat.id, text="Напиши /start это поможет!" )      
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn6 = types.KeyboardButton("👋 Поздороваться")
    btn7 = types.KeyboardButton("❓ Задать вопрос")
    markup.add(btn6, btn7)
    bot.send_message(message.chat.id,  text="Бот включен....".format(message.from_user), reply_markup=markup)
    

@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "👋 Поздороваться"):
        bot.send_message(message.chat.id, text="Привет!")
    elif (message.text == "❓ Задать вопрос"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn2 = types.KeyboardButton("⭐️Что я могу!")
        back = types.KeyboardButton("✈️Вернуться в главное меню")
        btn = types.KeyboardButton('🌌Мой ютуб канал!')
        btn8 = types.KeyboardButton("🌘Новый раздел!")
        markup.add( btn2,back,btn,btn8)
        bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)
   
    elif (message.text == "⭐️Что я могу!"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button166 = types.KeyboardButton("🔐Сгенирировать случайный пароль!")
        button117 = types.KeyboardButton("🛠Что же я могу?")
        buttont131 = types.KeyboardButton("✈️Вернуться обратно к кнопкам!")
        markup.add(button166, button117,buttont131)
        bot.send_message(message.chat.id, text="Ты попал в новый раздел!", reply_markup=markup)
   
    elif message.text == "🛠Что же я могу?":
         bot.send_message(message.chat.id, f'<code>{frase}</code>',  parse_mode="html")

    elif message.text == '🔐Сгенирировать случайный пароль!':
         password = ''
         for i in range(15):
            password += random.choice(chars)
         bot.send_message(message.chat.id, text=(f'''Ваш сгенирированный пароль: {password}'''))
    elif (message.text == "✈️Вернуться обратно к кнопкам!"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn22 = types.KeyboardButton("⭐️Что я могу!")
        back2 = types.KeyboardButton("✈️Вернуться в главное меню")
        btn2 = types.KeyboardButton('🌌Мой ютуб канал!')
        btn82 = types.KeyboardButton("🌘Новый раздел!")
        markup.add( btn22,back2,btn2,btn82)
        bot.send_message(message.chat.id, text="Ты вернулся!...", reply_markup=markup)

    elif (message.text == "🌘Новый раздел!"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button10 = types.KeyboardButton("🆘Выключить пк!")
        button11 = types.KeyboardButton("📺Скриншот рабочего стола!")
        buttont13 = types.KeyboardButton("✈️Вернуться обратно")
        buttont15 = types.KeyboardButton("🆘Перезагрузить пк!")
        markup.add(button10, button11,buttont13,buttont15,)
        bot.send_message(message.chat.id, text="Ты попал в новый раздел!", reply_markup=markup) 
    
    elif message.text == "🆘Выключить пк!":
         bot.send_message(message.chat.id, 'Выключаю....' '/start', reply_markup=types.ReplyKeyboardRemove())
         os.system("shutdown -s -t 0")        
   
    elif message.text == "🆘Перезагрузить пк!":
        bot.send_message(message.chat.id,text='Перезагружаю......' '/start',reply_markup=types.ReplyKeyboardRemove())
        os.system("shutdown -r -t 0")      
    
    elif message.text == "📺Скриншот рабочего стола!":
         image = pyscreenshot.grab()
         image.save("SPECIFY THE WAY TO SAVE SCREENSHOTS")
         bot.send_photo(message.chat.id, photo=open("SPECIFY THE WAY TO SAVE SCREENSHOTS",'rb'))
         bot.send_message(message.chat.id, text="Лови скриншот!")
    elif message.text == "📺Скриншот рабочего стола!":
         os.path.isfile("SPECIFY THE WAY TO SAVE SCREENSHOTS")
         os.remove("SPECIFY THE WAY TO SAVE SCREENSHOTS")     
    elif message.text == '🌌Мой ютуб канал!':
         bot.send_message(message.chat.id, text='https://www.youtube.com/channel/UCPzVuAKMI3Oah3ytYEXmUdw')
    elif (message.text == "✈️Вернуться обратно"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn22 = types.KeyboardButton("⭐️Что я могу!")
        back2 = types.KeyboardButton("✈️Вернуться в главное меню")
        btn2 = types.KeyboardButton('🌌Мой ютуб канал!')
        btn82 = types.KeyboardButton("🌘Новый раздел!")
        markup.add( btn22,back2,btn2,btn82)
        bot.send_message(message.chat.id, text="Ты вернулся!", reply_markup=markup)

    elif (message.text == "✈️Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("👋 Поздороваться")
        button2 = types.KeyboardButton("❓ Задать вопрос")
        button3 = types.KeyboardButton("🔚Выйти из режима кнопок!")
        markup.add(button1, button2,button3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню!", reply_markup=markup)
    elif message.text == "🔚Выйти из режима кнопок!":
         bot.send_message(message.chat.id, 'Выход успешный!' '/start', reply_markup=types.ReplyKeyboardRemove())  
    else:
     if (message.text == 'привет'):
        bot.send_message(message.chat.id, text="Ку братишка!)")
     else:
        bot.send_message(message.chat.id, message.text , parse_mode="html")

bot.polling(none_stop=True)
