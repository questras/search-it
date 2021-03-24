import requests

BASE_USER_AGENT = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:86.0) Gecko/20100101 Firefox/86.0'
DEFAULT_LANGUAGE = 'en'


class BaseSearch:
    base_url = None
    user_agent = BASE_USER_AGENT
    language = DEFAULT_LANGUAGE
    headers = {
        'user-agent': user_agent
    }

    def format_phrase(self, phrase: str) -> str:
        raise Exception('Not implemented')

    def create_url(self, phrase: str) -> str:
        raise Exception('Not implemented')

    def parse_request(self, request: requests.request) -> str:
        raise Exception('Not implemented')

    def search(self, phrase: str) -> str:
        phrase = self.format_phrase(phrase)
        url = self.create_url(phrase)

        r = requests.get(url, headers=BaseSearch.headers)
        r.raise_for_status()

        return self.parse_request(r)
