from abc import ABCMeta, abstractmethod
from bs4 import BeautifulSoup
import requests
from Formatter import Formatter


class AbstractScraper(metaclass=ABCMeta):

    def __init__(self):
        self.names = []
        self.f = Formatter()

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
        self.names = self.get_pokemon_cards(cards, 151)
        print(self.names)

    @staticmethod
    def get_pokemon_cards(cards, x):
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
        print('Scraping additional')
        for datum in url:
            soup = self.get_bs4_data(datum[1])
            vt = soup.find('table', attrs={'class': 'vitals-table'})
            rows = vt.find_all('td')
            indi = [row.text for row in rows[0:5]]
            t = self.f.type_formatter(indi[1])
            res = [indi[0], datum[0], t[0], t[1],
                   self.f.accent_remover(indi[2]), self.f.imp_remover(indi[3]),
                   self.f.imp_remover(indi[4]), datum[1]]
            print(res)


class Director(object):
    @staticmethod
    def go():
        f = Formatter()
        the_url = 'http://pokemondb.net/pokedex/'
        the_is = InitialScraper()
        the_is.scrape(the_url)

        the_list = f.add_url(the_is.names, the_url)

        the_ds = DetailScraper()
        the_ds.scrape(the_list)


if __name__ == "__main__":
    d = Director()
    d.go()
