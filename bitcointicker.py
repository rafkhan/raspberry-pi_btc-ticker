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

#infiniteloop = 1
while 1:
  #Clears LCD
	lcd.clear()
  #Loads data from standard MtGox API
	       #data = json.load(urllib2.urlopen('http://data.mtgox.com/api/2/BTCUSD/money/ticker_fast'))
	data = json.load(urllib2.urlopen('http://data.mtgox.com/api/1/BTCUSD/ticker'))
	#Formats date in standard YYYY-MM-DD HH-SS format
	lcd.message(datetime.now().strftime( '%F %H:%M\n'))
	#Displays and formats BTC/USD price from mtgox API response
	lcd.message( "BTC/USD: " + data["return"]["last"]["display"])
  #Sleeps for 30s
	sleep(30)