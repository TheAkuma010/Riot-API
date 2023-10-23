import requests

nomeinvocador = input("Digite o Nome de Invocador: ")

activesummoner = requests.get("https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + (nomeinvocador) + "?api_key=RGAPI-82f0756c-a360-467b-89d7-cfed8f3870b9")
summonerid = activesummoner.json()
specdata = requests.get("https://br1.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/" + (summonerid['id']) + "?api_key=RGAPI-82f0756c-a360-467b-89d7-cfed8f3870b9")
# (activesummoner.json())

print(summonerid['id'])
print(specdata.json())