import requests

nomeinvocador = input("Digite o Nome de Invocador: ")

activesummoner = requests.get("https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + (nomeinvocador) + "?api_key=")
summonerid = activesummoner.json()
specdata = requests.get("https://br1.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/" + (summonerid['id']) + "?api_key=")
# (activesummoner.json())

print(summonerid['id'])
print(specdata.json())
