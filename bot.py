import telebot

token = '1493667911:AAEQ0tlthdc1Ixg2Dc6S4NM6c2KTBLw6CSw'

bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
	bot.send_message(message.chat.id, 'Жопа')
	keyboard = telebot.types.ReplyKeyboardMarkup(True)
	keyboard.row('Привет', 'Пока', 'Иди в дупу')
	bot.send_message(message.chat.id, 'Твоя менюшка, сладкий!', reply_markup = keyboard)

@bot.message_handler(commands=['test'])
def start_message(message):
	markup = telebot.types.InlineKeyboardMarkup()
	markup.add(telebot.types.InlineKeyboardButton(text='Три', callback_data=3))
	markup.add(telebot.types.InlineKeyboardButton(text='Четыре', callback_data=4))
	markup.add(telebot.types.InlineKeyboardButton(text='Пять', callback_data=5))
	bot.send_message(message.chat.id, text="Какая средняя оценка была у Вас в школе?", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Шел бы ты отсюда, петушок!')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Ухожу ухожу красиво!')
    elif message.text.lower() == 'тревожность - это антиципация фрустрации актуализирующей потребности': 
    	bot.send_message(message.chat.id, 'Рита, не выебывайся!')
    elif message.text.lower() == 'кто котик?':
    	bot.send_message(message.chat.id, 'Рита котик, солнышко и самая красивая жэпка')
    else:
    	bot.send_message(message.chat.id, 'ХС ЖЕ')

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
	bot.answer_callback_query(callback_query_id=call.id, text='Спасибо за честный ответ!')
	answer = ''
	if call.data == '3':
		answer = 'Мое почтение!'
	elif call.data == '4':
		answer = 'Делаешь по красоте!'
	elif call.data == '5':
		answer = 'Диплом олимпудки лучше!'
	bot.send_message( call.message.chat.id, answer)


bot.polling()