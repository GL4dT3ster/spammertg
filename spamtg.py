from telethon.sync import TelegramClient, events

#from pyotp import TOTP

#if input ("Введите код из статьи: ") != TOTP("UC2UQZPN32334CZK").now():
#	exit(1)
#else:
#	print("Код верный")

#SERGOPROXY TG: @sergey0804,darksplit:SergoProxy
print(" 'TG-spam' - скрипт написан SergoProxy, для спама лс Telegram. \n Все вопросы и идеи в TG: @sergey0804. Данный скрипт был удален с GitHub и был перезалит GL4dT3ster`ом. Советую протестировать скрипт перед использованием.")
print()
hashtg = input('api_hash аккаунта: ')
iptg = int(input("api_id приложения: "))
px = int(input("Кол-во сообщений: "))
idp = input("ID пользователя: ")
mes = input("Текст сообщения: ")

api_id = iptg
api_hash = hashtg

with TelegramClient('proxy' , api_id, api_hash) as client:
	for i in range(px):
		client.send_message(idp, mes)
		client.send_message(idp, mes)
		client.send_message(idp, mes)
		client.send_message(idp, mes)
		client.send_message(idp, mes)
		
#SERGOPROXY TG: @sergey0804,darksplit:SergoProxy
