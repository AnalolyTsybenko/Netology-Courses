import requests
import bs4
import re
from user_agent import generate_navigator


KEYWORDS = ['дизайн', 'фото', 'web', 'python']

base_url = 'https://habr.com'
url = base_url + '/ru/all/'

HEADERS = generate_navigator()

response = requests.get(url, headers=HEADERS)
text = response.text


def find_articles(base_url_, keywords, text_, headers):
    pattern_ = '|'.join([fr'(\s{x}\s)' for x in keywords])
    soup = bs4.BeautifulSoup(text_, features='html.parser')
    articles = soup.find_all(class_='tm-articles-list__item')

    for article in articles:
        href = article.find(class_='tm-article-snippet__title-link').attrs['href']
        link = base_url_ + href
        res = requests.get(link, headers=headers).text
        articles_soup = bs4.BeautifulSoup(res, features='html.parser').text
        found = re.search(pattern_, articles_soup)
        if found:
            title = article.find(class_='tm-article-snippet__title tm-article-snippet__title_h2').text
            date = article.find('time').attrs['title']
            print(f'{date} - {title} - {link}')


if __name__ == '__main__':
    find_articles(base_url, KEYWORDS, text, HEADERS)
