# -*- coding: utf-8 -*-
import telebot

import os
from flask import Flask, request
from telebot import types

server = Flask(__name__)

bot = telebot.TeleBot('token')

@bot.message_handler(commands=['start'])
def start(message):
       sent = bot.send_message(message.chat.id, 'Добрый день. Мы поможем Вам доставить груз из Китая. Для начала давайте познакомимся. Как Вас зовут?')
       bot.register_next_step_handler(sent, hello)

#@bot.message_handler(func=lambda message: True, content_types=['text'])
#def echo_message(message):
 #   bot.reply_to(message, message.text)


def hello(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Достаточно', 'Недостаточно']])
    bot.send_message(message.chat.id, 'Привет, {name}. Рад Вас видеть. Пожалуйста, ответьте на несколько вопросов, '
                                      'нажимая на кнопки под окном ввода сообщения, и я подберу Вам нужного менеджера.'
                                      ' Первый вопрос самый основной - достаточно ли у Вас время на доставку?'.format(name=message.text),reply_markup=keyboard)
    bot.register_next_step_handler(message, name1)

def name1(message):
    if message.text == 'Достаточно':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in ['в Россию', 'в Европу']])
        bot.send_message(message.chat.id,'Ваш груз должен быть доставлен в Россию или в Европу и далее?',reply_markup=keyboard)
        bot.register_next_step_handler(message, name11)

    elif message.text == 'Недостаточно':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in ['ДА', 'НЕТ']])
        bot.send_message(message.chat.id, 'Вам нужно доставить очень срочно?', reply_markup=keyboard)
        bot.register_next_step_handler(message, name12)


def name11(message):
    if message.text == 'в Россию':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in ['Ростов', 'Владивосток', 'Москва', 'Екатеринбург']])
        bot.send_message(message.chat.id, 'Какой из городов в России ближе к Вам?', reply_markup=keyboard)
        bot.register_next_step_handler(message, name111)

    elif message.text == 'в Европу':
         bot.send_message(message.chat.id, 'Тогда мы можем доставить Ваш груз в Европу и далее. Мы довезем его в порт, в'
                                          ' Финляндии или в странах прибалтики.')
         markup = types.InlineKeyboardMarkup()
         switch_button = types.InlineKeyboardButton(text='менеджер по финскому морю', url= "https://t.me/Allrighthead")
         markup.add(switch_button)
         bot.send_message(message.chat.id,"Нажав на кнопку ниже, Вы попадете в чат с личным менеджером, спасибо за "
                                          "общение, было очень приятно познакомиться", reply_markup = markup)

def name111(message):
    if message.text == 'Ростов':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in ['в порту', 'до двери']])
        bot.send_message(message.chat.id,'Вы сможете забрать свой груз в порту Ростова или Вам необходима'
                                         ' доставка до двери?',reply_markup=keyboard)
        bot.register_next_step_handler(message, name1111)

    elif message.text == 'Владивосток':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in ['в порту', 'до двери']])
        bot.send_message(message.chat.id, 'Вы сможете забрать свой груз в порту Владивостока или Вам необходима'
                                          ' доставка до двери?', reply_markup=keyboard)
        bot.register_next_step_handler(message, name1111)

    elif message.text == 'Москва':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in ['в порту', 'до двери']])
        bot.send_message(message.chat.id, 'Вы сможете забрать свой груз в порту Москвы или Вам необходима'
                                          ' доставка до двери?',
                         reply_markup=keyboard)
        bot.register_next_step_handler(message, name1111)

    elif message.text == 'Екатеринбург':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in ['в порту', 'на вокзале', 'до двери']])
        bot.send_message(message.chat.id, 'Вы сможете забрать свой груз в порту или на вокзале Екатеринбурга'
                                          ' или Вам необходима доставка до двери?', reply_markup=keyboard)
        bot.register_next_step_handler(message, name1112)

def name1111(message):
    if message.text == 'в порту':
        bot.send_message(message.chat.id, 'Тогда мы можем доставить Ваш груз в порт этого города')
        markup = types.InlineKeyboardMarkup()
        switch_button = types.InlineKeyboardButton(text='менеджер по портам ростов, владик, москва', url="https://t.me/Allrighthead")
        markup.add(switch_button)
        bot.send_message(message.chat.id, "Нажав на кнопку ниже, Вы попадете в чат с личным менеджером, спасибо за "
                                          "общение, было очень приятно познакомиться", reply_markup=markup)

    elif message.text == 'до двери':
         bot.send_message(message.chat.id, 'Отлично, мы можем доставим груз прямо к Вам!')
         markup = types.InlineKeyboardMarkup()
         switch_button = types.InlineKeyboardButton(text='менеджер по автоперевозкам', url= "https://t.me/Allrighthead")
         markup.add(switch_button)
         bot.send_message(message.chat.id,"Нажав на кнопку ниже, Вы попадете в чат с личным менеджером, спасибо за "
                                          "общение, было очень приятно познакомиться", reply_markup = markup)

def name1112(message):
    if message.text == 'в порту':
        bot.send_message(message.chat.id, 'Тогда мы можем доставить Ваш груз в порт этого города')
        markup = types.InlineKeyboardMarkup()
        switch_button = types.InlineKeyboardButton(text='менеджер по портам екатеринбург', url="https://t.me/Allrighthead")
        markup.add(switch_button)
        bot.send_message(message.chat.id, "Нажав на кнопку ниже, Вы попадете в чат с личным менеджером, спасибо за "
                                          "общение, было очень приятно познакомиться", reply_markup=markup)

    elif message.text == 'до двери':
         bot.send_message(message.chat.id, 'Отлично, мы можем доставим груз прямо к Вам!')
         markup = types.InlineKeyboardMarkup()
         switch_button = types.InlineKeyboardButton(text='менеджер по автоперевозкам', url= "https://t.me/Allrighthead")
         markup.add(switch_button)
         bot.send_message(message.chat.id,"Нажав на кнопку ниже, Вы попадете в чат с личным менеджером, спасибо за "
                                          "общение, было очень приятно познакомиться", reply_markup = markup)
    elif message.text == 'на вокзале':
         bot.send_message(message.chat.id, 'Отлично, мы можем доставим груз на вокзал этого города!')
         markup = types.InlineKeyboardMarkup()
         switch_button = types.InlineKeyboardButton(text='менеджер по вокзалам', url= "https://t.me/Allrighthead")
         markup.add(switch_button)
         bot.send_message(message.chat.id,"Нажав на кнопку ниже, Вы попадете в чат с личным менеджером, спасибо за "
                                          "общение, было очень приятно познакомиться", reply_markup = markup)

def name12(message):
    if message.text == 'ДА':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in ['ДА', 'НЕТ']])
        bot.send_message(message.chat.id,'А бюджет это позволяет?',reply_markup=keyboard)
        bot.register_next_step_handler(message, name121)

    elif message.text == 'НЕТ':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in ['Москва', 'Санкт-Петербург','Владивосток','Екатеринбург','Новосибирск']])
        bot.send_message(message.chat.id, 'Какой из городов в России ближе к Вам?', reply_markup=keyboard)
        bot.register_next_step_handler(message, name122)

def name121(message):
    if message.text == 'ДА':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in ['ДА', 'НЕТ']])
        bot.send_message(message.chat.id,'Вы хотите перевезти опасный груз?',reply_markup=keyboard)
        bot.register_next_step_handler(message, name1211)

    elif message.text == 'НЕТ':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in ['Москва', 'Санкт-Петербург','Владивосток','Екатеринбург','Новосибирск']])
        bot.send_message(message.chat.id, 'Какой из городов в России ближе к Вам?', reply_markup=keyboard)
        bot.register_next_step_handler(message, name122)

def name1211(message):
    if message.text == 'ДА':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in ['в аэропорту', 'до двери']])
        bot.send_message(message.chat.id, 'Отлично, мы можем доставим груз к Вам на самолёте! Вы сможете забрать груз'
                                          ' в аэропорту или необходима доставка до двери?', reply_markup=keyboard)
        bot.register_next_step_handler(message, name12111)

    elif message.text == 'НЕТ':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in ['Москва', 'Санкт-Петербург','Владивосток','Екатеринбург','Новосибирск']])
        bot.send_message(message.chat.id, 'Какой из городов в России ближе к Вам?', reply_markup=keyboard)
        bot.register_next_step_handler(message, name122)

def name12111(message):
    if message.text == 'в аэропорту':
        bot.send_message(message.chat.id, 'Тогда мы можем доставить Ваш груз в аэропорт Вашего города')
        markup = types.InlineKeyboardMarkup()
        switch_button = types.InlineKeyboardButton(text='менеджер по аэропортам', url="https://t.me/Allrighthead")
        markup.add(switch_button)
        bot.send_message(message.chat.id, "Нажав на кнопку ниже, Вы попадете в чат с личным менеджером, спасибо за "
                                          "общение, было очень приятно познакомиться", reply_markup=markup)

    elif message.text == 'до двери':
         bot.send_message(message.chat.id, 'Мы можем доставим груз прямо к Вам!')
         markup = types.InlineKeyboardMarkup()
         switch_button = types.InlineKeyboardButton(text='менеджер по срочным автоперевозкам', url= "https://t.me/Allrighthead")
         markup.add(switch_button)
         bot.send_message(message.chat.id,"Нажав на кнопку ниже, Вы попадете в чат с личным менеджером, спасибо за "
                                          "общение, было очень приятно познакомиться", reply_markup = markup)

def name122(message):
    if message.text == 'Москва':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in ['на вокзале', 'до двери']])
        bot.send_message(message.chat.id,'Вы сможете забрать груз на вокзале Вашего города или необходима доставка до двери?',reply_markup=keyboard)
        bot.register_next_step_handler(message, name1221)

    elif message.text == 'Санкт-Петербург':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in ['на вокзале', 'до двери']])
        bot.send_message(message.chat.id,
                         'Вы сможете забрать груз на вокзале Вашего города или необходима доставка до двери?',
                         reply_markup=keyboard)
        bot.register_next_step_handler(message, name1221)

    elif message.text == 'Владивосток':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in ['в порту', 'до двери']])
        bot.send_message(message.chat.id,
                         'Вы сможете забрать груз в порту Вашего города или необходима доставка до двери?',
                         reply_markup=keyboard)
        bot.register_next_step_handler(message, name1222)

    elif message.text == 'Екатеринбург':
        bot.send_message(message.chat.id, 'Мы можем доставим груз прямо к Вам!')
        markup = types.InlineKeyboardMarkup()
        switch_button = types.InlineKeyboardButton(text='менеджер по автоперевозкам екатеринбург',
                                                   url="https://t.me/Allrighthead")
        markup.add(switch_button)
        bot.send_message(message.chat.id, "Нажав на кнопку ниже, Вы попадете в чат с личным менеджером, спасибо за "
                                          "общение, было очень приятно познакомиться", reply_markup=markup)

    elif message.text == 'Новосибирск':
        bot.send_message(message.chat.id, 'Мы можем доставим груз прямо к Вам!')
        markup = types.InlineKeyboardMarkup()
        switch_button = types.InlineKeyboardButton(text='менеджер по автоперевозкам новосибирск',
                                                   url="https://t.me/Allrighthead")
        markup.add(switch_button)
        bot.send_message(message.chat.id, "Нажав на кнопку ниже, Вы попадете в чат с личным менеджером, спасибо за "
        "общение, было очень приятно познакомиться", reply_markup = markup)

def name1221(message):
        if message.text == 'на вокзале':
            bot.send_message(message.chat.id, 'Тогда мы можем доставить Ваш груз на вокзал Вашего города')
            markup = types.InlineKeyboardMarkup()
            switch_button = types.InlineKeyboardButton(text='менеджер по вокзалам москва, спб', url="https://t.me/Allrighthead")
            markup.add(switch_button)
            bot.send_message(message.chat.id, "Нажав на кнопку ниже, Вы попадете в чат с личным менеджером, спасибо за "
                                              "общение, было очень приятно познакомиться", reply_markup=markup)

        elif message.text == 'до двери':
            bot.send_message(message.chat.id, 'Мы можем доставим груз прямо к Вам!')
            markup = types.InlineKeyboardMarkup()
            switch_button = types.InlineKeyboardButton(text='менеджер по автоперевозкам москва, спб',
                                                       url="https://t.me/Allrighthead")
            markup.add(switch_button)
            bot.send_message(message.chat.id, "Нажав на кнопку ниже, Вы попадете в чат с личным менеджером, спасибо за "
                                              "общение, было очень приятно познакомиться", reply_markup=markup)


def name1222(message):
    if message.text == 'в порту':
        bot.send_message(message.chat.id, 'Тогда мы можем доставить Ваш груз в порт Владивостока')
        markup = types.InlineKeyboardMarkup()
        switch_button = types.InlineKeyboardButton(text='менеджер по порту владивостока',
                                                   url="https://t.me/Allrighthead")
        markup.add(switch_button)
        bot.send_message(message.chat.id, "Нажав на кнопку ниже, Вы попадете в чат с личным менеджером, спасибо за "
                                          "общение, было очень приятно познакомиться", reply_markup=markup)

    elif message.text == 'до двери':
        bot.send_message(message.chat.id, 'Мы можем доставим груз прямо к Вам!')
        markup = types.InlineKeyboardMarkup()
        switch_button = types.InlineKeyboardButton(text='менеджер по автоперевозкам владивосток',
                                                   url="https://t.me/Allrighthead")
        markup.add(switch_button)
        bot.send_message(message.chat.id, "Нажав на кнопку ниже, Вы попадете в чат с личным менеджером, спасибо за "
                                          "общение, было очень приятно познакомиться", reply_markup=markup)

@bot.message_handler(commands=['help'])
def start(message):
    sent = bot.send_message(message.chat.id, 'Чем я могу Вам помочь?')
    bot.register_next_step_handler(sent, help)

def help(message):
        bot.send_message(
            message.chat.id,
            'Попробую передать Ваше сообщение нашему отвественному менеджеру')

@server.route("/bot", methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url="https://chat3test.herokuapp.com/bot")
    return "!", 200

server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
server = Flask(__name__)