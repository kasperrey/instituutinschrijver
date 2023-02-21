class School:
    def __init__(self, naam, niet_indicator_leerlingen, indicator_leerlingen):
        self.naam = naam
        self.niet_indicator_leerlingen = niet_indicator_leerlingen
        self.indicator_leerlingen = indicator_leerlingen
        self.indicator = []
        self.niet_indicator = []


class Scholen:
    def __init__(self, *args):
        self.list = []
        for x in args:
            self.list.append(x)
