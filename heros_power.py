import requests

def most_intelligence():
    heros_names = ['Hulk', 'Captain America', 'Thanos']
    max_intelligence = 0
    max_intelligent = 'Hulk'
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    response = requests.get(url)
    heros = response.json()
    for hero in heros :
        if hero['name'] in heros_names:
            if hero['powerstats']['intelligence'] > max_intelligence:
                max_intelligence = hero['powerstats']['intelligence'] 
                max_intelligent = hero['name'] 
    print(max_intelligent) 