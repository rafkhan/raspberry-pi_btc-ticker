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

##### API calls and selection

##### Bitcoin #####
BTC = json.load(urllib2.urlopen('http://data.mtgox.com/api/1/BTCUSD/ticker'))
BTC_currentprice = BTC["return"]["last"]["value"]
BTC_result = BTC["result"]
# >1000 rollover
if (int(round(float(mtgox_currentprice))) > 1000):
    BTC_finalprice = int(round(float(mtgox_currentprice)))
else:
	BTC.finalprice = mtgox_currentprice
#Error handling
if BTC_result != "success":
	print "fail"
	lcd.message("MtGox API error")
# Function
def BTC():
    lcd.clear()
    time = datetime.now().strftime( '%F %H:%M\n' )
    lcd.message(time)
    lcd.message( "BTC/USD: " + "$" + BTC_currentprice)
    sleep(30)
BTC()


#Dogecoin (DOGE)
#DOGE = json.load(urllib2.urlopen('http://pubapi.cryptsy.com/api.php?method=singlemarketdata&marketid=132'))
#DOGE_currentprice = DOGE["markets"]["DOGE"]["lasttradeprice"]
#DOGE_result = DOGE["success"]
