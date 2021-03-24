import requests
from bs4 import BeautifulSoup

green = '\033[92m'
red = '\033[91m'
endcolor = '\033[0m'

base_url = 'https://www.google.com/search?'
user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:86.0) Gecko/20100101 Firefox/86.0'
headers = {
    'user-agent': user_agent,
}

def search(phrase: str, language: str = 'en'):
    url = f'{base_url}q={phrase}&hl={language}'
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    soup = BeautifulSoup(r.content, 'html.parser')
    container = soup.find(id='kp-wp-tab-overview')

    if container:
        result = container.find('span').get_text()
        return result
    else:
        return 'No result'


phrase = input('Enter phrase: ').replace(' ', '+')

print(search(phrase))
