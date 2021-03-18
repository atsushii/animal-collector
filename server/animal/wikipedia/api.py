import requests
from bs4 import BeautifulSoup

class AnimalDataProcessing:

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

    def extract_animal_name_and_description(self, class_id='firstHeading', soup=None, class_name='mw-parser-output'):
        try:
            animal_name = soup.find(id=class_id).text
            p_tag_list = soup.find('div', class_=class_name)
            description = p_tag_list.findChildren('p', recursive=False)[2].text
        except AttributeError as err:
            print(err)

        return animal_name, description

    def main(self):
        soup = self.parse_html()
        animal_name, description = self.extract_animal_name_and_description(soup=soup)

        return animal_name, description

if __name__=='__main__':
    a = AnimalDataProcessing('tiger')
    a.main()


