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

while 1:
        lcd.clear()
        data = json.load(urllib2.urlopen('http://data.mtgox.com/api/1/BTCUSD/ticker'))
        time = datetime.now().strftime( '%F %H:%M\n' )
        lcd.message(time)
        lcd.message( "BTC/USD: " + data["return"]["last"]["display"])
        sleep(30)

##### Code Snippets
# API call and selection
mtgox = json.load(urllib2.urlopen('http://data.mtgox.com/api/1/BTCUSD/ticker'))
mtgox_currentprice = mtgox["return"]["last"]["value"]
mtgox_result = mtgox["result"]

# Checks if price > 1000
if (int(round(float(mtgox_currentprice))) > 1000):
	over1000 = int(round(float(mtgox_currentprice)))

#If result != "success", write error message
if mtgox_result != "success":
	print "fail"
	lcd.message("MtGox API error")
#####



