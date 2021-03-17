import requests
from bs4 import BeautifulSoup

class AnimalDataProcessing:

    def __init__(self, animal_name):
        self.url = f'https://en.wikipedia.org/wiki/{animal_name}'
        self.animal_name = animal_name

    def parse_html(self):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, 'html.parser')
        name = soup.find(id='firstHeading')
        print(name.text)


if __name__=='__main__':
    a = AnimalDataProcessing('cat')
    a.parse_html()


