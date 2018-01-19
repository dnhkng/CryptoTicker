import hd44780_nodemcu
from time import sleep
import urequests
from machine import Pin

up_char = bytearray([0x04, 0x0E, 0x1F, 0x04, 0x04, 0x04, 0x04, 0x00])

down_char = bytearray([0x04, 0x04, 0x04, 0x04, 0x1F, 0x0E, 0x04, 0x00])


class Ticker:
	def __init__(self):
		self.screen = hd44780_nodemcu.Screen(pins=[Pin(0), Pin(4), Pin(5), Pin(16)], 
			en_pin=Pin(12), rs_pin=Pin(15), rows=4, cols=16)
		
		# Create pre-filled list for indexing
		self.symbol = [None, None, None, None]
		self.price = [0, 0, 0, 0]
		self.old_price = [0, 0, 0, 0]

		self.screen.createChar(0, up_char)
		self.screen.createChar(1, down_char)

	def refresh(self, seconds=60):
		while(True):
			# display results every 'seconds' seconds
			self.update()
			print('Updated')
			sleep(seconds)


	def update(self):
		try:
			# Get the top 4 cryptocurrencies:
			r = urequests.get("https://api.coinmarketcap.com/v1/ticker/?limit=4")
			json_data = r.json()
			# it's mandatory to close response objects as soon as you finished working with them.
			r.close()


			# Update data
			self.old_price = self.price[:]

			for i in range(4):
				self.symbol[i] = json_data[i]['symbol']
				self.price[i] = json_data[i]['price_usd']

		except:
			return

		# Update LCD
		self.draw()

	def draw(self):
		# clear
		self.screen.clear()

		# Draw each line
		for i in range(4):
			self.screen.setCursor(i, 0)
			self.screen.println('   ' + self.symbol[i] + ' ')
			if self.price[i] == self.old_price[i]:
				self.screen.println('=')
			elif float(self.price[i]) > float(self.old_price[i]):
				self.screen.write_byte(0, char_mode=True)
			else:
				self.screen.write_byte(1, char_mode=True)

			self.screen.println(" $" + self.price[i])