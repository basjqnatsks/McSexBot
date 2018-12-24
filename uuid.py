import requests
class uuid:
	def get(self, account):
		JsonUUID = requests.get('https://api.mojang.com/users/profiles/minecraft/' + str(account))
		return JsonUUID.json()['id']
