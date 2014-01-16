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

file = open("debug.txt")


while 1:
	lcd.clear()
	data = json.load(urllib2.urlopen('http://data.mtgox.com/api/1/BTCUSD/ticker'))
	time = datetime.now().strftime( '%F %H:%M\n' )
	lcd.message(time)
	lcd.message( "BTC/USD: " + data["return"]["last"]["display"])
	sleep(30)