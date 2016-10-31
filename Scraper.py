from abc import ABCMeta, abstractmethod
from bs4 import BeautifulSoup
import requests
from Formatter import Formatter


class AbstractScraper(metaclass=ABCMeta):

    def __init__(self):
        self.names = []

    @abstractmethod
    def scrape(self, url):
        pass

    @staticmethod
    def get_bs4_data(url):
        r = requests.get(url).text
        return BeautifulSoup(r, 'html.parser')


class InitialScraper(AbstractScraper):
    def scrape(self, url):
        print('Scraping Main')
        soup = self.get_bs4_data(url + 'national')
        table = soup.find('div', attrs={'class': 'infocard-tall-list'})
        cards = table.find_all('span')
        self.names = self.get_pokemon_cards(cards, 10)
        # dex_data = self.format_dex(dex_data)
        # self.set_nat_dex(dex_data)
        print(self.names)

    def get_pokemon_cards(self, cards, x):
        data = []
        c = 0
        for card in cards:
            stuffs = card.find_all(['a', 'small'])
            if c < x:
                data.append(stuffs[2].text)
                c += 1
        return data


class DetailScraper(AbstractScraper):

    def scrape(self, url):
        pass


class Director(object):
    @staticmethod
    def go():
        f = Formatter()
        the_url = 'http://pokemondb.net/pokedex/'
        the_is = InitialScraper()
        the_is.scrape(the_url)

        the_list = f.add_url(the_is.names, the_url)
        print(the_list)
        # the_ds = DetailScraper(the_list)


if __name__ == "__main__":
    d = Director()
    d.go()
