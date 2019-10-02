import pyowm
import telebot

owm = pyowm.OWM('2dbd4d8ae880ca5737375946c337f14d', language="uk")
bot = telebot.TeleBot("622175106:AAGdwBvo9Gq15qUOIgN6Y0aAlfF8GaQAoOg")


@bot.message_handler(content_types=['text'])
def send_echo(message):
    observation = owm.weather_at_place(message.text)
    w = observation.get_weather()
    temp = w.get_temperature('celsius')["temp"]
    answer = "В місті " + message.text + " зараз " + w.get_detailed_status() + "\n"
    answer += "Температура: " + str(temp) + "\n\n"
    bot.send_message(message.chat.id, answer)


bot.polling(none_stop=True)
