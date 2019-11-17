#!/usr/bin/python

# --
# Copyright NoweEnergie.org
# --

import smtplib
import time
from email.mime.text import MIMEText
from config import *


#wczytanie wiadomosci
fm = open('message.txt', 'r')
m_content = fm.read()

#wczytanie listy maili
f = open('mails.txt', 'r')
#zliczenie maili
total_mails = len(file('mails.txt').readlines()) 
#wczytanie maili do tablicy
x=1
mail_list = ['']
for line in f:
  mail_list += [line.rstrip('\n')]
  x=x+1

#zerowanie licznika wyslanych maili
sended_mails = 1

#polaczenie z serwerem
mailServer = smtplib.SMTP(smtpserver,587)
mailServer.ehlo()
mailServer.starttls()
mailServer.ehlo()
mailServer.login(smtpuser, smtppass)

#czy jest polaczony
isconnect = 1

#wysylanie maila na kazdy adres
while(sended_mails<total_mails):
        print "wysylanie do "+mail_list[sended_mails]+" ["+str(sended_mails)+" z "+str(total_mails)+"]"
	
	r = mail_list[sended_mails]
	RECIPIENTS = [r]

	msg = MIMEText(m_content+'\n')
	msg['Subject'] = SUBIECT
	msg['From'] = SENDER
	msg['To'] = mail_list[sended_mails]

	if isconnect == 0 :
		mailServer = smtplib.SMTP(smtpserver,587)
		mailServer.ehlo()
		mailServer.starttls()
		mailServer.ehlo()
		mailServer.login(smtpuser, smtppass)
	
	try:
		mailServer.sendmail(smtpuser,RECIPIENTS,msg.as_string())
		time.sleep(1)
	except:
		print "----UTRACONO POLACZENIE - PONAWIAM WYSYLANIE ZA 10s----"
		mailServer.close()
		time.sleep(10)
		sended_mails = sended_mails - 1
		isconnect = 0

	sended_mails = sended_mails + 1	

