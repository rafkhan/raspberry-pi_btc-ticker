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
       (lcd.UP , 'Sita sings\nthe blues' , lcd.BLUE),
       (lcd.DOWN , 'I see fields\nof green' , lcd.GREEN),
       (lcd.RIGHT , 'Purple mountain\nmajesties', lcd.VIOLET),
       (lcd.SELECT, '' , lcd.ON))
prev = -1
while True:
    for b in btn:
        if lcd.buttonPressed(b[0]):
            if b is not prev:
                lcd.clear()
                lcd.message(b[1])
                lcd.backlight(b[2])
                prev = b
            break