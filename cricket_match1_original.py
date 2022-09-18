import requests, time


def AvailableMsg():
	url0 = 'https://api.telegram.org/bot5659173779:AAF97iKhqw4MwiLt8M9y-gUxk-9oAlJvO0I/sendMessage?chat_id=-1001759600352&text=Tickets Available Now!'
	url1 = 'https://api.telegram.org/bot5659173779:AAF97iKhqw4MwiLt8M9y-gUxk-9oAlJvO0I/sendMessage?chat_id=-1001759600352&text=Tickets Available Now!\nClick here to buy - https://insider.in/mastercard-series-3rd-t20i-india-v-australia-hyderabad-sep25/buy'

	for i in range(10):
		requests.get(url0)

	requests.get(url1)
		

def ErrorMsg():
	url2 = f'https://api.telegram.org/bot5659173779:AAF97iKhqw4MwiLt8M9y-gUxk-9oAlJvO0I/sendMessage?chat_id=5174886440&text=Error {response}'
	for i in range(20):
		requests.get(url2)
		

match_page = 'https://insider.in/mastercard-series-3rd-t20i-india-v-australia-hyderabad-sep25/buy'

stop = 1

while stop:

	html = requests.get(match_page)
	response = str(html)

	if response == '<Response [404]>':
		print('Not Available')
		time.sleep(10)
		
	elif response == '<Response [200]>':
	    AvailableMsg()
	    stop = 0
                
	else:
		ErrorMsg()
		stop=0
