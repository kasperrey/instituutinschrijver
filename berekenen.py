import random
import pikle_databank
from scholen import Scholen
from leerlingen import Leerlingen


class System:
    def __init__(self):
        self.hoeveelste = 1
        self.scools: Scholen = pikle_databank.load_school()
        self.leerlingen: Leerlingen = pikle_databank.load_leerlingen()
        self.plek_geven()
        self.sorteren()
        for x in self.scools.list:
            print(f"de leerlingen van {x.naam} zijn")
            for y in x.indicator:
                print(y.naam)
            for y in x.niet_indicator:
                print(y.naam)

    def plek_geven(self):
        for x in self.scools.list:
            for y in self.leerlingen.list:
                if y.list[0] == x.naam:
                    if y.indicator:
                        x.indicator.append(y)
                    elif not y.indicator:
                        x.niet_indicator.append(y)
                    else:
                        raise TypeError("foute inschrijf data")

    def niet_uit_lijst(self):
        for x in self.scools.list:
            if x.indicator_leerlingen < len(x.indicator):
                return True
            elif x.niet_indicator_leerlingen < len(x.niet_indicator):
                return True
        return False

    def sorteren(self):
        while self.niet_uit_lijst():
            list_over = []
            for x in self.scools.list:
                random.shuffle(x.indicator)
                random.shuffle(x.niet_indicator)
                indicator_leerlingen = x.indicator_leerlingen
                niet_indicator_leerlingen = x.niet_indicator_leerlingen
                over = x.indicator_leerlingen - len(x.indicator)
                if over < 0:
                    for y in range(0, abs(over)):
                        x.niet_indicator.append(x.indicator[indicator_leerlingen])
                        x.indicator.pop(indicator_leerlingen)

                over = niet_indicator_leerlingen - len(x.niet_indicator)
                if over < 0:
                    for y in range(0, abs(over)):
                        list_over.append(x.niet_indicator[niet_indicator_leerlingen])
                        x.niet_indicator.pop(niet_indicator_leerlingen)

            for x in list_over:
                if x.indicator:
                    for y in self.scools.list:
                        if x.list[self.hoeveelste] == y.naam:
                            y.indicator.append(x)
                else:
                    for y in self.scools.list:
                        if x.list[self.hoeveelste] == y.naam:
                            y.niet_indicator.append(x)
            self.hoeveelste += 1


s = System()
