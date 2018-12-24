import library
import requests
class OPcape:
	def __init__(self, debug):
		self.debug = debug
		array = []
		open('OPCAPE_OUT.txt', 'w')
		file_name = input('Input File Name (Defaults To file.txt EMAIL:PASS:IGN): ')
		if file_name == '':
			file_name = 'file.txt'
		accounts = library.readIT().f(file_name)
		for x in range(len(accounts)):
			array.append(accounts[x].split(':'))

		for x in range(len(accounts)):
			try:
				respoisne = requests.get('http://s.optifine.net/capes/'+array[x][2]+'.png')
				if int(respoisne.status_code) == 200:
					out = open('OPCAPE_OUT.txt', 'a')
					out.write(array[x][0] + ":" + array[x][1] + ':' + array[x][2] + "\n")
			except:
				pass