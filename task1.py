import requests

TOKEN = ""

urls = [
    f'https://superheroapi.com/api/{TOKEN}/search/Hulk',
    f'https://superheroapi.com/api/{TOKEN}/search/Thanos',
    f'https://superheroapi.com/api/{TOKEN}/search/Captain%America',
]

def get_requests(all_url):
    request = (requests.get(url) for url in all_url)
    return request

def parse():
    superman = []
    for item in get_requests(urls):
        intelligence = item.json()
        try:
            for power_stats in intelligence['results']:
                superman.append({
                    'name': power_stats['name'],
                    'intelligence': power_stats['powerstats']['intelligence'],
                })
        except KeyError:
            print(f'Error urls: {urls}')

    intelligence_superhero = 0
    name = ''
    for intelligence_hero in superman:
        if intelligence_superhero < int(intelligence_hero['intelligence']):
            intelligence_superhero = int(intelligence_hero['intelligence'])
            name = intelligence_hero['name']

    print(f"Самый интеллектуальный {name}, интеллект: {intelligence_superhero}")



if __name__ == '__main__':
    parse()