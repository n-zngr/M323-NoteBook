import random

def shuffle(a):
    def random_sample(x, l):
        return random.sample(l, x)
    return random.sample(a, len(a))

def pick(l):
    def inner_pick(x):
        samples = random.sample(l, x)
        list(map(lambda item: print("*", item), samples))
    return inner_pick

spices = ["Zimt", "Kreuzkümmel", "Koriander", "Gewürznelke", "Kardamom, am besten sowohl grün als auch schwarz", "Schwarze Pfefferkörner", "Rote Chilischoten oder Chilipulver", "Ingwerpaste oder frischen Ingwer, kein Ingwerpulver", "Garam Masala", "Kurkuma"]
base = ["Glasig angebratene Zwiebeln", "Naturjoghurt mit Crème fraîche versetzt", "Currypaste aus der Migros", "Grünes Curry vom Thai-Corner meines Vertrauens", "Kokosnussmilch"]
ingredients = ["Geflügel", "Lamm", "Blumenkohl und Kartoffeln", "Paneer", "Auberginen", "Kefen oder Bohnen"]

print("Curry benötigt zunächst eine feuchte Basis. Ich schlage vor, folgende Basis zu benutzen:\n")
pick(base)(1)

print("\nDie Gewürze werden in einer Pfanne aromageröstet. Als mögliche Gewürze bieten sich an:\n")
pick(spices)(5)

print("\nWir kommen jetzt zur Hauptzutat. Bei unserem Curry ist das\n")
pick(ingredients)(1)

print("\nDie Hauptzutat wird in einer gesonderten Pfanne bei hoher Hitze angebraten und dann mit der flüssigen Basis und den Gewürzen zusammen bei niedriger Hitze schmoren lassen, bis das Curry gut eingekocht und servierfertig ist.\n")
print("Guten Appetit!")