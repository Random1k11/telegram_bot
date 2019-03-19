# This example uses Python 2.7+ and the python-request library
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import logging

FORMAT_LOG = '%(asctime)s, %(levelname)s, %(name)s, %(filename)s, %(funcName)s, сообщение: %(message)s'
logger = logging.basicConfig(level=logging.DEBUG, filename='coin_market.log', format=FORMAT_LOG,
							 filemode='w')

def get_info_about_AllCoins():
	url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
	parameters = {
	  'start': '1',
	  'limit': '5000',
	  'convert': 'USD',
	}
	headers = {
	  'Accepts': 'application/json',
	  'X-CMC_PRO_API_KEY': '5f9a808c-5962-4f32-8d53-57cc98ca08dc',
	}
	session = Session()
	session.headers.update(headers)

	try:
	  logging.info('Пытаюсь сделать запрос')
	  response = session.get(url, params=parameters)
	  data = json.loads(response.text)
	  data = data['data']
	  with open('coin_market.json', 'w') as f:
		  json.dump(data, f, indent=2)
		  logging.info('Запрос прошел успешно. Файл записан')

	except (ConnectionError, Timeout, TooManyRedirects) as e:
	  logging.error('Ошибка запроса')
	  print(e)
	return data


def parsing_info_coins(name_coin=None):
	coin_names = []
	for get_info in get_info_about_AllCoins():
		coin_names.append(get_info['name'].lower())
		if name_coin != None and get_info['name'].lower() == name_coin.lower():
			get_info = round(get_info['quote']['USD']['price'], 2)
			response_message = (name_coin + ': ' + str(get_info) + ' USD')
			return response_message
	if name_coin == None:
		return coin_names
	else:
		return 'Нет монеты с таким названием'




if __name__ == "__main__":
	print(parsing_info_coins('bitcoin1'))
