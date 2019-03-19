from flask import Flask
#from flask_sslify import SSLify
from flask import request
from flask import jsonify
import requests
import json
from coin_market import *



app = Flask(__name__)
#sslify = SSLify(app)

URL = 'https://api.telegram.org/bot408697626:AAHW5D48WVfee5zTT3nZmQ58OPsauhLhVzA/'

def get_updates():
    #https://api.telegram.org/bot408697626:AAHW5D48WVfee5zTT3nZmQ58OPsauhLhVzA/getUpdates
    url = URL + 'getUpdates'
    r = requests.get(url)
    write_json(r.json())
    return r.json()

#URL = 'https://api.telegram.org/bot789891284:AAE4GbYXqzaXw1m9-wn98jLozOY5Hll5hb8/'

def write_json(data, filename='answer.json'):
	with open(filename, 'w') as f:
	   json.dump(data, f, indent=2, ensure_ascii=False)



def send_message(chat_id, text='Привет я БОТ'):
    url = URL + 'sendMessage'
    answer = {'chat_id': chat_id, 'text':text}
    r = requests.post(url, json=answer)
    return r.json()


def send_cryptocurrency_rate(chat_id, message):
    for name_coin in parsing_info_coins():
        if name_coin in message:
            send_message(chat_id, parsing_info_coins(name_coin))

#
# def request_to_yandex(chat_id, message):
#     url = 'https://yandex.ru/search/?text=' + message
#     r = requests.get(url).text
#     print(r)
#     def searsh_message_in_yandex(r):
#         soup = BeautifulSoup(r, 'lxml')
#         search = soup.find('span', class_='text-cut2 typo typo_text_m typo_line_m')
#         if search is None:
#             send_message(chat_id, text='Не понимаю что это такое...')
#         else:
#             search = search.text.split()[:-1]
#             search = ' '.join(search)
#             send_message(chat_id, search)
#     searsh_message_in_yandex(r)



# @app.route('/', methods=['POST', 'GET'])
# def index():
#     if request.method == 'POST':
#         r = request.get_json()
#         chat_id = r['message']['chat']['id']
#         message = r['message']['text'].lower().split()
#         send_cryptocurrency_rate(chat_id, message)
#     #request_to_yandex(chat_id, ' '.join(message))
#         #create_buttons()
#         return jsonify(r)
#     return '<h1>Hello bot!!!</h1>'


if __name__ == '__main__':
    while True:
	    get_updates()
