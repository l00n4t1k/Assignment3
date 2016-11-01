from Pokemon import Pokemon


class Builder(object):

    def build(self):
        pass

    def get(self):
        pass


class PokemonBuilder(Builder):
    def __init__(self):
        self.pokemon = Pokemon()

    def build(self, data):
        self.pokemon.set_num(data[0])
        self.pokemon.set_name(data[1])
        self.pokemon.set_weight(data[2])
        self.pokemon.set_height(data[3])
        self.pokemon.set_url(data[4])
        self.pokemon.set_type1(data[5])
        self.pokemon.set_type2(data[6])

    def get(self):
        return self.pokemon
