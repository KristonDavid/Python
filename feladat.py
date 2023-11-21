import json

adatbazis = []

<<<<<<< HEAD
# hoppákupon
with open("database.json", "r", encoding="utf8") as fájl:
    adatbazis = json.load(fájl)
=======
with open("database.json", "r", encoding="utf8") as fájl:
    adatbazis = json.loads(fájl)
>>>>>>> aa014fe97f1c34a7041a7e6c453ee7e620767ce8

print(adatbazis)