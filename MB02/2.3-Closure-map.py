maximalePunkte = 100

def prozent(x):
   def prozent_x(y):
      return x * y
   return prozent_x

def punkte_liste(liste, faktor):
   prozent_f = prozent(faktor)
   return list(map(prozent_f, liste))

liste = [10, 12, 3, 23, 4, 5, 11, 2]
print(punkte_liste(liste, (maximalePunkte / 100)))
