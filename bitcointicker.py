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
		raise Exception("MtGox API call failed!")
 
	current_price = mtgox["return"]["last"]["value"]

	# > $1000 rollover, Rounds/Converts to int
	if (int(round(float(current_price))) > 1000):
		final_price = int(round(float(current_price)))
	else:
		final_price = current_price
	return final_price

while 1:
	lcd.clear()
	#Calls BTC function, gets time and formats.
	try:
		price = BTC()
	except Exception:
		lcd.message("MtGox API call failed! :(")

	time = datetime.now().strftime( '%F %H:%M\n' )
	#Displays time on first line, BTC/USD rate on next line.
	lcd.message(time)
	lcd.message( "BTC/USD: " + "$" + price)
	#Sleeps until next API call can be made. 
	sleep(30)
