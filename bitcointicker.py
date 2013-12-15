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
	print "Clearing LCD"
	lcd.clear()
	#data = json.load(urllib2.urlopen('http://data.mtgox.com/api/2/BTCUSD/money/ticker_fast'))
	print "Loading data from MtGox API"
	data = json.load(urllib2.urlopen('http://data.mtgox.com/api/1/BTCUSD/ticker'))
	# Formats date in standard YYYY-MM-DD HH-SS format
	print "Displaying date"
	lcd.message(datetime.now().strftime( '%F %H:%M\n'))
	# Displays and formats BTC/USD price from mtgox API response
	print "Displaying data"	
	lcd.message( "BTC/USD: " + data["return"]["last"]["display"])
	print "Sleeping for 30 seconds"
	sleep(30)
	print "Waking from nap, yawn"

##### Late night stoned code in an attempt to get color to change maintaining text while button press

if __name__ == '__main__':

    lcd = Adafruit_CharLCDPlate()
    lcd.begin(16, 2)
    lcd.clear()
    lcd.message("Adafruit RGB LCD\nPlate w/Keypad!")
    sleep(1)

    col = (('Red' , lcd.RED) , ('Yellow', lcd.YELLOW), ('Green' , lcd.GREEN),
           ('Teal', lcd.TEAL), ('Blue' , lcd.BLUE) , ('Violet', lcd.VIOLET),
           ('Off' , lcd.OFF) , ('On' , lcd.ON))

    print "Cycle thru backlight colors"
    for c in col:
       print c[0]
       lcd.clear()
       lcd.message(c[0])
       lcd.backlight(c[1])
       sleep(0.5)

    btn = ((lcd.SELECT, 'Select', lcd.ON),
           (lcd.LEFT , 'Left' , lcd.RED),
           (lcd.UP , 'Up' , lcd.BLUE),
           (lcd.DOWN , 'Down' , lcd.GREEN),
           (lcd.RIGHT , 'Right' , lcd.VIOLET))
    
    print "Try buttons on plate"
    lcd.clear()
    lcd.message("Try buttons")
    prev = -1
    while True:
        for b in btn:
            if lcd.buttonPressed(b[0]):
                if b is not prev:
                    print b[1]
                    lcd.clear()
                    lcd.message(b[1])
                    lcd.backlight(b[2])
                    prev = b
                break
