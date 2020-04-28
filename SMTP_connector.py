import smtplib
import db_read
import os

from dotenv import load_dotenv

project_folder = os.path.expanduser('~/Projects/plant-pull')
load_dotenv(os.path.join(project_folder, '.env'))

gmail_user = os.getenv("GMAIL_USER")
gmail_password = os.getenv("GMAIL_PASSWORD")

try:
    server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server_ssl.ehlo()
    server_ssl.login(gmail_user, gmail_password)
except:
    print ('Something went wrong...')

sent_from = gmail_user
to = []

begonias_in_stock = db_read.check_begonias()

if begonias_in_stock:
	email_text = ''''''
	for begonia in begonias_in_stock:
		if begonia != begonias_in_stock[-1]:
			email_text += "{} - {} (${})\n".format(begonia[1], begonia[2], begonia[3])
		else:
			email_text += "{} - {} (${})".format(begonia[1], begonia[2], begonia[3])
		
	print(email_text)
	server_ssl.sendmail(sent_from, to, str(email_text))
	server_ssl.close()

	print ('Email sent!')