# CryptoTicker
Micropython ESP8266 Ticker for displaying Crypo prices on a HD44780 LCD


Powered by [CoinMarketCap](http://www.CoinMarketCap.com) and their free [JSON API](https://coinmarketcap.com/api/).

The Top 4 Coins (by market Cap) prices are updated, and the price movement and current price are displaed on the LCD.

Prices are updated around every 5 minutes on the Coinmarket Cap API.

![Image of Ticker](https://raw.githubusercontent.com/dnhkng/CryptoTicker/master/media/ticker.jpg)


## Initial setup

1. Copy the files to your ESP8266 board
	* using WebREPL
		* See [ESP8266 QuickRef](http://docs.micropython.org/en/latest/esp8266/esp8266/quickref.html#webrepl-web-browser-interactive-prompt)
	* using ampy
		* see [Adafruit ampy guide](https://learn.adafruit.com/micropython-basics-load-files-and-run-code/file-operations)

2. Connect to WiFi, credentials are persisted, so you wont need to enter them each time

	```
	>>> import network
	>>> sta_if = network.WLAN(network.STA_IF);
	>>> sta_if.active(True)
	>>> sta_if.scan()
	>>> sta_if.connect("ssid","pass")
	>>> sta_if.isconnected()
	```

	Disable the AP, unless you need it.

	```
	>>> ap_if = network.WLAN(network.AP_IF)
	>>> ap_if.active(False)
	```

3. Install urequests with upip. You need to be on WiFi for this to work.

	```
	>>> import upip
	>>> upip.install('micropython-urequests')
	```

4. Restart, and the program will be running.
	If you break the program with CTRL-C at the REPL,
	you can get a single update with:
	```
	t.update()
	```	
	Or restart the program, specifying an update rate is seconds (default is 60):
	```
	t.refresh(10)
	```


## Parts

* [NodeMCU](https://www.aliexpress.com/wholesale?catId=0&SearchText=nodemcu) € 2.50
* [HD44780 module](https://www.aliexpress.com/wholesale?catId=0&SearchText=hd44780+20x4) € 2.50


![Image of Board](https://raw.githubusercontent.com/dnhkng/CryptoTicker/master/media/board.jpg)


## Connections

The two circuit boards can be soldered together directly, just by bending a few header pins and using a little wire.

NodeMCU       | HD44780 module
------------- | ---------------
Gnd           | 1 VSS 
3V            | 2 VDD
Gnd           | 3 VE (Contrast voltage) 
D8 (GPIO15)   | 4 RS (Register Select)
Gnd           | 5 RW (Read/Write)
D6 (GPIO12)   | 6 EN (Enable)
nc            | 7 nc
nc            | 8 nc
nc            | 9 nc
nc            | 10 nc
D3 (GPIO0)    | 11 D4
D2 (GPIO0)    | 12 D5
D1 (GPIO0)    | 13 D6
D0 (GPIO0)    | 14 D7
3V            | 15 A (BackLight Anode)
Gnd           | 16 K (Backlight Cathode)

## Links

* [MicroPython HD44780 Driver](https://github.com/CRImier/MicroPython-modules)
* [NodeMCU](https://en.wikipedia.org/wiki/NodeMCU)
* [micropython.org](http://micropython.org)

## Credits

* Inspired by [MicroPython ESP8266 Nokia 5110 Bitcoin Price Index](https://github.com/mcauser/MicroPython-ESP8266-Nokia-5110-Bitcoin)
* Bitcoin Logo [Wikipedia](https://commons.wikimedia.org/wiki/File:Bitcoin_logo.svg) (Creative Commons CC0 1.0)
