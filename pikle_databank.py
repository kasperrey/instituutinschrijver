import os
import pickle
from leerlingen import Leerlingen
from scholen import Scholen


def load_leerlingen() -> Leerlingen:
    load = open(os.path.expanduser('~') + '/Desktop/Kasper Projecten/instituut inschrijver/school_data', 'rb')
    kinderen: Leerlingen = pickle.load(load)
    load.close()
    return kinderen


def save_leerlingen(leerlingen: Leerlingen):
    s = open(os.path.expanduser('~') + '/Desktop/Kasper Projecten/instituut inschrijver/school_data', 'wb')
    pickle.dump(leerlingen, s)
    s.close()


def load_school() -> Scholen:
    load = open(os.path.expanduser('~') + '/Desktop/Kasper Projecten/instituut inschrijver/scholen', 'rb')
    kinderen: Scholen = pickle.load(load)
    load.close()
    return kinderen


def save_school(school: Scholen):
    s = open(os.path.expanduser('~') + '/Desktop/Kasper Projecten/instituut inschrijver/scholen', 'wb')
    pickle.dump(school, s)
    s.close()
