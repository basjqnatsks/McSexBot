import library
import base64
from time import sleep
import requests
class cape:
	def __init__(self):
		var = []
		self.method = 'https'
		self.proxies = self.CheckProxyFile()
		with open('file.txt', 'r') as f:
			open('Skin.txt', 'w')
			ff = f.read().split('\n')
		for x in range(len(ff)):
			var.append(ff[x].split(':'))
		m = open('Skin.txt', 'a')
		for x in range(len(var)):
			try:
				var[x][2]
				while True:
					try:
						response = requests.get('https://sessionserver.mojang.com/session/minecraft/profile/' + str(var[x][2]), proxies={})
						print(response.json())
						print('\n')
						var = base64.b64decode(response.json()['properties'][0]['value'])
					except:
						sleep(6)
					else:
						if 'CAPE' in str(var):
							m.write(var[x][0]+":"+var[x][1]+":     " + str(1) + "\n")
						else:
							m.write(var[x][0]+":"+var[x][1]+":    "+ str(0) + "\n")
						break
				
			except:
				pass
	def CheckProxyFile(self):
		try:
			ProxiesFile = library.readIT().f(filename="proxies.txt")
		except:
			raise FileExistsError("Hey Dipshit! Try Getting Some Proxies (proxies.txt)")
		return ProxiesFile
