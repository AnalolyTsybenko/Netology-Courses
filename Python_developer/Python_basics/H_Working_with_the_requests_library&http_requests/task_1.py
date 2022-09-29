import requests


def the_smartest_hero(url: str, heroes: list):
    response = requests.get(url).json()
    hero_name = ''
    hero_intelligence = 0
    for hero in response:
        if hero['name'] in heroes and hero['powerstats']['intelligence'] > hero_intelligence:
            hero_intelligence = hero['powerstats']['intelligence']
            hero_name = hero['name']
    return f'Кто самый умный супергерой?\n{hero_name} (intelligence - {hero_intelligence})'


if __name__ == '__main__':
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    heroes = ['Hulk', 'Captain America', 'Thanos']
    print(the_smartest_hero(url, heroes))
