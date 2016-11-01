from abc import ABCMeta, abstractmethod
from bs4 import BeautifulSoup
import requests
from Formatter import Formatter
from Builder import PokemonBuilder


class AbstractScraper(metaclass=ABCMeta):

    def __init__(self):
        self.names = []
        self.f = Formatter()

    @abstractmethod
    def do_scrape(self, url):
        pass

    @staticmethod
    def get_bs4_data(url):
        r = requests.get(url).text
        return BeautifulSoup(r, 'html.parser')


class InitialScraper(AbstractScraper):
    def do_scrape(self, url):
        print('Scraping Main')
        soup = self.get_bs4_data(url + 'national')
        table = soup.find('div', attrs={'class': 'infocard-tall-list'})
        cards = table.find_all('span')
        self.names = self.get_pokemon_cards(cards, 12)
        # print(self.names)

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

    def do_scrape(self, url):
        print('Scraping additional')
        res = []

        for datum in url:
            print("Scraping", datum[0])
            soup = self.get_bs4_data(datum[1])
            vt = soup.find('table', attrs={'class': 'vitals-table'})
            rows = vt.find_all('td')
            indi = [row.text for row in rows[0:5]]
            t = self.f.type_formatter(indi[1])
            info = [int(indi[0]), datum[0], t[0], t[1],
                    self.f.accent_remover(indi[2]),
                    float(self.f.imp_remover(indi[3])),
                    float(self.f.imp_remover(indi[4])), datum[1]]
            # print(info)
            p = PokemonBuilder()
            p.build(info)
            res.append(p.get())
        return res


class Director(object):
    @staticmethod
    def go():
        f = Formatter()
        the_url = 'http://pokemondb.net/pokedex/'
        the_is = InitialScraper()
        the_is.do_scrape(the_url)

        the_list = f.add_url(the_is.names, the_url)

        the_ds = DetailScraper()
        the_dex = the_ds.do_scrape(the_list)
        for element in the_dex:
            print(element.get_name())


if __name__ == "__main__":
    d = Director()
    d.go()
