import library
from OptifineCape import OPcape
from Wynnchecker import wynncraft
from Cracker import crackIT
import os


def listCommands():
	print("1> crack   			[God?]")
	print("2> wynn				[Wynncraft Processer Takes The Format Email:Pass:CURRENT_IGN]")
	print("3> opcape			[Checks For Optifine Cape Takes The Format Email:Pass:CURRENT_IGN]")
	print("0> exit         		[exit the program]")


if __name__ == "__main__":
	os.system('cls')
	os.system('title  ')
	userInput=''
	debug = 0
	while userInput.lower() != "exit":
		debugmod = debug % 2
		listCommands()
		userInput = input("Sex?>>> ")
		try:
			int(userInput)
		except:
			userInput = userInput.lower()
		else:
			userInput = int(userInput)
		if userInput == "clear" or userInput == "cls":
			os.system('cls')
		elif userInput == "crack" or userInput == 1:
			crackIT(debugmod)
		elif userInput == "wynn" or userInput == 2:
			wynncraft(debugmod)
			os.system('cls')
		elif userInput == "opcape" or userInput == 3:
			OPcape(debugmod)
			os.system('cls')
		elif userInput == "debug":
			if debug % 2 == 0:
				os.system('title Debug Mode')
			else:
				os.system('title  ')
			debug += 1 
		elif userInput == "exit" or userInput == 0:
			break
		else:
			print("Invalid command!")
		userInput=''