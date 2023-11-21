import json

adatbazis = []

# hoppákupon
with open("database.json", "r", encoding="utf8") as fájl:
    adatbazis = json.load(fájl)

# tesztelt
print(adatbazis)