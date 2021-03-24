import requests

from bs4 import BeautifulSoup

from base.base import BaseSearch


class GoogleSearch(BaseSearch):
    base_url = "https://www.google.com/search?"

    def format_phrase(self, phrase: str) -> str:
        return phrase.replace(" ", "+")

    def create_url(self, phrase: str) -> str:
        return f"{GoogleSearch.base_url}q={phrase}&hl={GoogleSearch.language}"

    def parse_request(self, request: requests.request) -> str:
        soup = BeautifulSoup(request.content, "html.parser")
        container = soup.find(id="kp-wp-tab-overview")

        if container:
            result = container.find("span").get_text()
            return result
        else:
            return "No result"
