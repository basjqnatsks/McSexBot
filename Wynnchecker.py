import library
import os
from uuid import uuid
from PreviousName import prev_name
import requests



class wynncraft:
	def __init__(self, debug):
		if debug == 1:
			self.debug = True
		else:
			self.debug = False
		self.accountfile = self.open_accountfile()
		self.accounts_length = len(self.accountfile)
		self.accounts_parsed = self.account_parser()
		self.final = []
		self.names = []
		self.sort = []
		if self.debug:
			print(self.accounts_parsed)
		self.grab_alterative_Names()
		self.grab_level()
		os.system('title  ')
	def account_parser(self):
		TempArray = self.accountfile
		for x in range(self.accounts_length):
			TempArray[x] = self.accountfile[x].split(":")
		return TempArray
	
	def open_accountfile(self):
		while True:
			accountfile = input("Name Of Account File (Defaults to file.txt EMAIL:PASS:IGN): ")
			if accountfile == '':
				accountfile = "file.txt"
			try:
				accountfile = str(accountfile)
			except TypeError:
				continue
			else:
				if '.txt' not in accountfile:
					accountfile = accountfile + '.txt'
				accountfile = library.readIT().f(filename=accountfile)
				return accountfile

	def grab_alterative_Names(self):
		
		for i in range(self.accounts_length):
			os.system('title Getting Names ['+str(i)+"/"+str(self.accounts_length)+"] Getting Levels [0/" +str(self.accounts_length)+"]")
			try:
				UUID = uuid().get(self.accounts_parsed[i][2])
				self.final.append([self.accounts_parsed[i][0], self.accounts_parsed[i][1], self.accounts_parsed[i][2]])

				_names = prev_name().get(UUID)

				self.names.append(_names)
			except:
				pass


	def grab_level(self):

		for i in range(self.accounts_length):
			os.system('title Getting Names ['+str(self.accounts_length)+"/"+str(self.accounts_length)+"]   Getting Levels ["+str(i)+"/" +str(self.accounts_length)+"]")
			try:
				count = 0
				for x in range(len(self.names[i])):
					JSON = requests.get('https://api.wynncraft.com/public_api.php?action=playerStats&command=' + str(self.names[i][x]))
					try:	
						count += int(JSON.json()['global']['total_level'])
					except:
						pass
				self.final[i].append(count)	
			except:
				pass
		for x in range(len(self.final)):
			try:
				if self.final[x][3] > 1:
					self.sort.append([self.final[x][0], self.final[x][1], self.final[x][2], self.final[x][3]])
					#f.write(str(self.final[x][0]) + ":" + str(self.final[x][1]) + "   " + str(self.final[x][2]) + '\n')
			except:
				pass
		self.sorta()
		for x in range(len(self.sort)):
			f = open('wynndata.txt', 'a')
			f.write(str(self.sort[x][0]) + ":" + str(self.sort[x][1]) + ":"+str(self.sort[x][2])+"   " + str(self.sort[x][3]) + '\n')
	def sorta(self):
		while True:
			kcount = 0
			for xy in range(len(self.sort) -1):
				try:
					if self.sort[xy][3] < self.sort[xy + 1][3]:
						temp = self.sort[xy]
						self.sort[xy] = self.sort[xy + 1]
						self.sort[xy + 1] = temp
						kcount += 1
				except:
					pass
			if self.debug:
				print(kcount)
			if kcount == 0:
				break