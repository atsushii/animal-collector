import requests
from bs4 import BeautifulSoup


class AnimalDataProcessing(object):

    def __init__(self, animal_name):
        self.url = f'https://en.wikipedia.org/wiki/{animal_name}'
        self.animal_name = animal_name

    def parse_html(self):
        try:
            page = requests.get(self.url)
            soup = BeautifulSoup(page.content, 'html.parser')
        except requests.exceptions.RequestException as err:
            raise SystemExit(err)

        return soup

    def extract_animal_description(self, soup=None, class_name='mw-parser-output', **kwargs):
        try:
            p_tag_list = soup.find('div', class_=class_name)
            description = p_tag_list.findChildren('p', recursive=False)[2].text
        except AttributeError as err:
            raise err

        return description

    def scraper(self):
        soup = self.parse_html()
        description = self.extract_animal_description(soup=soup)

        return description
