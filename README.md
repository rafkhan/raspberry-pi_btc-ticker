Raspberry-Pi-BTC-Ticker
=======================

####Purpose
One day I got tired of pulling up bitcoin.clarkmoody or MtGox every time I wanted to check the BTC/USD rate, so I ordered a [16x2 RGB LCD kit from adafruit](http://www.adafruit.com/products/1109), soldered it up, then wrote some python code for my RPi that displays the current rate from MtGox, called every 30s (Limit with standard Mtgox API). I find myself checking it every few minutes when I'm home, which could be a good or bad thing.

####Ideas for future expansion:            
	- Change display color based on market uptick/downtick.                   
	- Dimming backlight during certain timeslots (While the human is sleeping)          
	- Recovery from dropped wireless connection / API call failure.                  
	- Support for LTC + DOGE + altcoin price tickers (Controllable by button press)         
	- Sound notification based on adjustable thresholds.
	- EMA 10/21 strategy notification.
	- Change RGB LCD to a VFD display to reduce glare/light pollution.  
	
####Psychological Effects
Aside from the alien blue glow at 3AM, and knowing the price of bitcoin nearly 24/7, surprisingly little has changed. Knowing the EXACT price of bitcoin is reassuring when trading, but I find the data is difficult to keep in my memory, so I think some kind of 1 hour/24 hour averaging would be beneficial as a second menu option.

Will report back if I experience a singularity with the blockchain.
