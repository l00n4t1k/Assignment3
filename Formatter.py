import re


class Formatter(object):

    @staticmethod
    def hash_stripper(the_list):
        res = []
        for datum in the_list:
            datum[0] = datum[0].strip('#')
            res.append(datum)
        return res

    @staticmethod
    def type_formatter(the_list):
        res = []
        for datum in the_list:
            if datum[2].find(' · ') == -1:
                datum.append('')
            else:
                tl = datum[2].split(' · ')
                datum[2] = tl[0]
                datum.append(tl[1])
            res.append(datum)
        return res

    def add_url(self, the_list, the_url):
        new_list = []
        for datum in the_list:
            datum = self.accent_remover(datum)
            if re.search('♀', datum):
                datum = 'Nidoran-f'
            elif re.search('♂', datum):
                datum = 'Nidoran-m'
            elif re.search('Farfetch\'d', datum):
                datum = 'Farfetchd'
            elif re.search('Mr. Mime', datum):
                datum = 'Mr-Mime'
            elif re.search('Mime Jr.', datum):
                datum = 'Mime-Jr'
            new_url = the_url + datum
            new_list.append(new_url)
        return new_list

    # duplicate code / speculative generality
    @staticmethod
    def comma_remover(i):
        p = re.compile(',')
        i = p.sub('/', i)
        return i

    @staticmethod
    def accent_remover(i):
        p = re.compile('é')
        i = p.sub('e', i)
        return i

    @staticmethod
    def imp_remover(i, c):
        n = re.search(r'\d*[.]\d*' + c, i)
        return n.group()

    @staticmethod
    def get_gen(the_list, the_min, the_max):
        the_res = []
        for datum in the_list[the_min:the_max]:
            the_res.append(datum)
        return the_res

    @staticmethod
    def readability_formatter(the_list):
        res = []
        head = ['Number', 'Name', 'Type', '', 'Address', 'Species', 'Height',
                'Weight', 'Local Number(s)']
        the_list.insert(0, head)
        for datum in the_list:
            cur_line = str(datum[0]) + ', ' + str(datum[1]) + ', ' + \
                       str(datum[2])
            if datum[3] != '':
                cur_line += '/' + str(datum[3])
            cur_line += ', ' + str(datum[4]) + ', ' + str(datum[5]) + ', ' + \
                        str(datum[6]) + ', ' + str(datum[7])
            if re.search('—', datum[8]):
                cur_line += ', ' + ''
            else:
                cur_line += ', ' + str(datum[8])
            res.append(cur_line)
        return res
