import requests, time
# import schedule


def AvailableMsg():
	url1 = 'https://api.telegram.org/bot5659173779:AAF97iKhqw4MwiLt8M9y-gUxk-9oAlJvO0I/sendMessage?chat_id=5174886440&text=Tickets Available Now!\nClick here to buy - https://insider.in/mastercard-series-3rd-t20i-india-v-australia-hyderabad-sep25/buy'

	for i in range(15):
		requests.get(url1)
		

# schedule.every().day.at(":00:00").do(AvailableMsg)
		

def NotAvailableMsg():
	url2 = 'https://api.telegram.org/bot5659173779:AAF97iKhqw4MwiLt8M9y-gUxk-9oAlJvO0I/sendMessage?chat_id=5174886440&text=Still not opened!'
	for i in range(2):
		requests.get(url2)
		

match_page = 'https://insider.in/mastercard-series-3rd-t20i-india-v-australia-hyderabad-sep25/buy'

x=1

while x:

	html = requests.get(match_page)
	response = str(html)

	# print(html)
	# print(response)

	if response == '<Response [404]>':
		print('Not Available')
		time.sleep(5)
		AvailableMsg()
	else:
		AvailableMsg()
		x=0
