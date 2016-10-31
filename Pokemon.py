
class Pokemon(object):
    def __init__(self):
        self.number = 0
        self.name = ""
        self.weight = 0
        self.height = 0
        self.url = ""
        self.type1 = ""
        self.type2 = ""

    def set_num(self, num):
        self.number = num

    def set_name(self, name):
        self.name = name

    def set_weight(self, weight):
        self.weight = weight

    def set_height(self, height):
        self.weight = height

    def set_url(self, url):
        self.url = url

    def set_type1(self, the_type):
        self.type1 = the_type

    def set_type2(self, the_type):
        self.type2 = the_type

    def get_num(self):
        return self.number

    def get_name(self):
        return self.name

    def get_weight(self):
        return self.weight

    def get_height(self):
        return self.weight

    def get_url(self):
        return self.url

    def get_type1(self):
        return self.type1

    def get_type2(self):
        return self.type2
