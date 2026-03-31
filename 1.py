import telebot

TOKEN = "8653624522:AAEjNMXBaW2jxF3JCSPjz6Q1hVO-JrZjQf0"
bot = telebot.TeleBot(TOKEN)
bot.remove_webhook()

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет, я EnkaBot!")

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.send_message(message.chat.id, message.text)

print("✅ Бот запущен!")
bot.infinity_polling()