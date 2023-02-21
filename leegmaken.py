import pikle_databank
from leerlingen import Leerlingen
from scholen import Scholen, School


pikle_databank.save_leerlingen(Leerlingen())
wawa = School('wawa', 3, 1)
koe = School('koe', 2, 1)
zwijnstijn = School('BCR colege', 4, 2)
vliegje = School('vliegje', 1, 1)
blork = School('blork', 2, 1)
ha_hmmm = School('ha hmmm', 3, 2)
scholen = Scholen(wawa, koe, zwijnstijn, vliegje, blork, ha_hmmm)
pikle_databank.save_school(scholen)
