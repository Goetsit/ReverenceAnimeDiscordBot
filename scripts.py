import json
import requests
import secrets
import auth
import random

#
# parameters = {
#  auth.CLIENT_ID
# }
#
# root = requests.get("https://api.myanimelist.net/v2/anime?q=one&limit=4", params=parameters)
#
#
# print(root.json())
def jprint(obj):
 text = json.dumps(obj, sort_keys=True, indent=4)
 return text


print("Now generating computer's choice...")
computer_choice = random.randint(1, 9000)
url_builder = 'https://api.jikan.moe/v4/anime/'
url_builder = url_builder + str(computer_choice)
print(url_builder)
computer_response = requests.get(url_builder)
#print(computer_response.json())
#print("computer's choice: ", computer_response.json()['results'])

anime_loader = jprint(computer_response.json())
anime = json.loads(anime_loader)

# for item in anime["data"]:
anime_data = anime["data"]
print(anime_data)


#print(jprint(computer_response.json()))