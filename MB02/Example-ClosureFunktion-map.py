# Modul 323-sw2: Beispiel 3 -  Closure mit map()
# Multipliziert eine Liste von Zahlen mit einem Faktor

def mal(x):
   def mal_x(y):
      return x * y
   return mal_x

def mult_liste(liste, faktor):
   mal_f = mal(faktor)
   return list(map(mal_f, liste))         # list() ist ein Type-Casting auf ein Listenobjekt.

li = [10, 12, 3, 23, 4, 5, 11, 2]
print(mult_liste(li, 10))
