# Modul 323-sw3: Beispiel4
# Listenverarbeitung mit zip()
# Zip verarbeitet mehrere Listen zu einer Liste mit Tupeln der entsprechenden Elemente aller Teillisten

liste1 = ["Hänsel", "Max", "Susi", "Bonny", "Batman", "Dick", "Peter"]
liste2 = ["Gretel", "Moritz", "Strolch", "Clide", "Robin", "Doof"] 

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
l2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
l3 = [3,  6,  9, 12, 15, 18, 21, 24, 27, 30]  

res1 = list(zip(l1, l2, l3))

print(res1)

res2 = list(zip(liste1, liste2))

print(res2)