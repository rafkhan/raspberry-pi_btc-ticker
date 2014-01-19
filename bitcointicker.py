 #!/usr/bin/python
 
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
from subprocess import *
from time import sleep, strftime
from datetime import datetime
 
import json
import urllib2
import time

lcd = Adafruit_CharLCDPlate()
lcd.begin(16,1)
 
def BTC():
	mtgox = json.load(urllib2.urlopen('http://data.mtgox.com/api/1/BTCUSD/ticker'))
	if mtgox["result"] != "success":
		lcd.message("MtGox API failed!")
		raise Exception("MtGox API failed!")
 
	current_price = mtgox["return"]["last"]["value"]

	# > $1000 rollover, Rounds/Converts to int
	if (int(round(float(current_price))) > 1000):
		final_price = int(round(float(current_price)))
	else:
		final_price = current_price
	return final_price

def DOGE():
	cryptsy = json.load(urllib2.urlopen('http://data.mtgox.com/api/1/BTCUSD/ticker'))
	if cryptsy["result"] != "1":
		lcd.message("Cryptsy API failed!")
		raise Exception("Cryptsy API failed!")

	current_price = cryptsy["return"]["markets"]["DOGE"]["lasttradeprice"]
	# No rollover necessary, but need to figure out how to deal with decimal places
	return final_price

#Add support for switching between currencies by using button code
while 1:
	lcd.clear()
	#Calls BTC function, gets time and formats
	price = BTC()
	time = datetime.now().strftime( '%F %H:%M\n' )
	#Displays time on first line, BTC/USD rate on next line
	lcd.message(time)
	lcd.message( "BTC/USD: " + "$" + price)
	#Sleeps until next API call is possible
	#Needs to be customized per API, add support next
	sleep(30)
