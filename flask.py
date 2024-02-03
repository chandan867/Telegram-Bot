from flask import Flask, request
import telebot

bot = telebot.TeleBot('Bot Access Token')

app = Flask(__name__)

@app.route('/')
def check():
    return 'I am running fine, how About you'


@app.route('/webhook', methods=['POST'])
def webhook():
    message = request.get_json()
    chat_id = message['message']['chat']['id']
    user_input = message['message']['text']
    first_word = user_input.split()[0]
    bot.send_message(chat_id, first_word)
    return 'ok'

if __name__ == '__main__':
    app.run(port=8181)
