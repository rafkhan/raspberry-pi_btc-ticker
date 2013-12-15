#!~/usr/bin/python

# Allows handling URL and API return data in JSON
import urllib2
import json
from datetime import datetime

# API call to MtGox BTC/USD ticker
data = json.load(urllib2.urlopen('http://data.mtgox.com/api/1/BTCUSD/ticker')	)

# API call returns JSON formatted response. Format.
ticker = data["return"]["last"]["display"

# Timestamp
time = datetime.now().strftime('%b %d %H:%M:%S - ')

# Print everything on LCD.
print timestamp + ticker

# Hope for a graceful exit
exit()
