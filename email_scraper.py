import requests
from bs4 import BeautifulSoup
import smtplib
URL = 'https://www.amazon.in/dp/B00BFDR9DW/ref=cm_sw_r_other_apa_i_SCndEb13226MS'
headers = {"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/79.0.3945.79 Chrome/79.0.3945.79 Safari/537.36"}

def send_mail(title, price):
	print(title)
	print(price)
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login('ritwik.chakradhar1994@gmail.com' , 'irkdctbavliikynr')
	subject = 'The price for Lindt Assorted Nuts fell down!'
	body = 'Check the Amaon Link - https://www.amazon.in/dp/B00BFDR9DW/ref=cm_sw_r_other_apa_i_SCndEb13226MS'
	msg = 'Subject : {}\n\n{}'.format(subject,body)
	server.sendmail('ritwik.chakradhar1994@gmail.com' , 'contact2shaista@gmail.com', msg)
	print("Email has been sent!")
	server.quit() 	

check = requests.get(URL, headers = headers)

content = BeautifulSoup(check.content, 'html.parser')

title = content.find(id = 'productTitle').get_text().strip()


price = float(content.find(id = 'priceblock_ourprice').get_text().strip().replace(',','')[2:])


if(price < 900):
	send_mail(title, price)

