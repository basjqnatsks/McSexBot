import requests
class prev_name:
	def get(self, UUID):
		Json = requests.get('https://api.mojang.com/user/profiles/' + str(UUID) + '/names')
		Array = []
		for x in range(len(Json.json())):
			Array.append(Json.json()[x]['name'])
		return Array
