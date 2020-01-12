import telegram
import os
import sys

#token that can be generated talking with @BotFather on telegram
my_token = 'Yout bot token'

def send(msg, chat_id, token=my_token):
	"""
	Send a mensage to a telegram user specified on chatId
	chat_id must be a number!
	"""
	bot = telegram.Bot(token=token)
	bot.sendMessage(chat_id=chat_id, text=msg)


# proxy setting ##################
proxy = 'http://178.62.232.133:3128/' #some proxy I found

os.environ['http_proxy'] = proxy
os.environ['HTTP_PROXY'] = proxy
os.environ['https_proxy'] = proxy
os.environ['HTTPS_PROXY'] = proxy

# from subprocess import call
# print(call(["wget",  "-q", "-O", "-", "checkip.dyndns.org"]))

###################################

send(sys.argv[1], "yours chat id") #TODO: make to tool to find chatid out