Raspberry-Pi-BTC-Ticker
=======================

One day I got tired of pulling up bitcoin.clarkmoody or MtGox every time I wanted to check the BTC/USD rate, so I ordered a 16x2 RGB LCD kit from adafruit, soldered it up, then wrote some python code for my RPi that displays the current rate from MtGox, called every 30s (Limit with standard Mtgox API)

I find myself checking it every few minutes when I am home, which could be a good or bad thing.


Ideas for future expansion include;                
	- Change display color based on market uptick/downtick.                   
	- Dimming backlight during certain timeslots (While the human is sleeping)          
	- Recovery from dropped wireless connection / API call failure.                  
	- Support for LTC + other altcoin price tickers (Controllable by button press)         
	- Sound notification based on adjustable thresholds.              
	- EMA 10/21 strategy notification.                 
