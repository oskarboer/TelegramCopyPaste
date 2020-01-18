import telegram
import os
import sys

#token that can be generated talking with @BotFather on telegram

cred = open('/home/nequus/Documents/Programing/TelegramCopyPaste/my_credentials.txt', 'r')

my_token = str(cred.readline().rstrip())
my_chat_id = int(cred.readline().rstrip())

def send(msg, chat_id, token=my_token):
	bot = telegram.Bot(token=token)
	if os.path.exists(msg) and os.path.isfile(msg):
		bot.send_document(chat_id=chat_id, document=open(msg, 'rb'))
	else:
		bot.sendMessage(chat_id=chat_id, text=msg)


# proxy setting, should be in this format proxy = 'http://51.68.121.144:3128/', notice the http:// / part ################## 
proxy = 'http://51.68.121.144:3128/'

os.environ['http_proxy'] = proxy
os.environ['HTTP_PROXY'] = proxy
os.environ['https_proxy'] = proxy
os.environ['HTTPS_PROXY'] = proxy

# from subprocess import call
# print(call(["wget",  "-q", "-O", "-", "checkip.dyndns.org"]))

###################################

send(sys.argv[1], my_chat_id)