import pikle_databank

kinderen = pikle_databank.load_leerlingen()
naam = input("naam?")
for x in kinderen.list:
    if x.naam == "Kasper Reynders":
        kinderen.list.remove(x)

for x in kinderen.list:
    print(x.naam)

pikle_databank.save_leerlingen(kinderen)
