import requests, time


def AvailableMsg(stop_available):
	if stop_available == 1:
		url0 = 'https://api.telegram.org/bot5659173779:AAF97iKhqw4MwiLt8M9y-gUxk-9oAlJvO0I/sendMessage?chat_id=-1001759600352&text=Tickets Available Now!'
		url1 = 'https://api.telegram.org/bot5659173779:AAF97iKhqw4MwiLt8M9y-gUxk-9oAlJvO0I/sendMessage?chat_id=-1001759600352&text=Tickets Available Now!\nClick here to buy - https://insider.in/mastercard-series-3rd-t20i-india-v-australia-hyderabad-sep25/buy'

		for i in range(10):
			requests.get(url0)

		requests.get(url1)
	else:
		print('Tickets released! Stop executing.')
		

def ErrorMsg():
	url2 = f'https://api.telegram.org/bot5659173779:AAF97iKhqw4MwiLt8M9y-gUxk-9oAlJvO0I/sendMessage?chat_id=5174886440&text={i} Error {response}'
	for i in range(20):
		requests.get(url2)
		

match_page = 'https://insider.in/mastercard-series-3rd-t20i-india-v-australia-hyderabad-sep25/buy'

stop = 1
stop_available = 1

while stop:

	html = requests.get(match_page, allow_redirects=True)
	response = str(html)

	if response == '<Response [404]>':
		print('Tickets not available yet!')
		time.sleep(10)
		
	elif response == '<Response [200]>':
		AvailableMsg(stop_available)
		stop_available = 0
                
	else:
		ErrorMsg()
		stop=0
