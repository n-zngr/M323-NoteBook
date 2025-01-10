import random

def shuffle(a):
    rand = 0
    index = 0
    shuffled = []
    
    for value in a:
        rand = random.randint(0, index)
        shuffled.insert(rand, value)
        index += 1
        
    return shuffled

def random_sample(x, l):
    return shuffle(l)[:x]  # return-Wert ist eine Liste [:x] ist Slicing-Variante für gewünschte Anzahl Elemente!

def pick(l):
    def inner_pick(x):
        samples = random_sample(x, l)
        for item in samples:
            print("*", item)
    return inner_pick

spices = [
    "Zimt",
    "Kreuzkümmel",
    "Koriander",
    "Gewürznelke",
    "Kardamom, am besten sowohl grün als auch schwarz",
    "Schwarze Pfefferkörner",
    "Rote Chilischoten oder Chilipulver",
    "Ingwerpaste oder frischen Ingwer, kein Ingwerpulver",
    "Garam Masala",
    "Kurkuma"
]
base = [
    "Glasig angebratene Zwiebeln",
    "Naturjoghurt mit Crème fraîche versetzt",
    "Currypaste aus der Migros =/",
    "Grünes Curry vom Thai-Corner meines Vertrauens"
    "Kokosnussmilch"
]
ingredients = [
    "Geflügel",
    "Lamm",
    "Blumenkohl und Kartoffeln",
    "Paneer",
    "Auberginen",
    "Kefen opder Bohnen"
]

print("Curry benötigt zunächst eine feuchte Basis. Ich schlage vor, folgende Basis zu benutzen:\n")
pick(base)(1)

print("\nDie Gewürze werden in einer Pfanne aromageröstet. Als mögliche Gewürze bieten sich an:\n")
pick(spices)(5)

print("\nWir kommen jetzt zur Hauptzutat. Bei unserem Curry ist das\n")
pick(ingredients)(1)

print("\nDie Hauptzutat wird in einer gesonderten Pfanne bei hoher Hitze angebraten und dann mit der flüssigen Basis und den Gewürzen zusammen bei niedriger Hitze schmoren lassen, bis das Curry gut eingekocht und servierfertig ist.\n")
print("Guten Appetit!")