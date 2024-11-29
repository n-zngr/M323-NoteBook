# Verwende dafür ausschliesslich Anweisung und Konzepte, die Du bereits kennst
# Zur Erstellung der Zahlenliste kannst Du die Funktion randint(a,b) aus der Bibliothek random verwenden. 

import random as rd

def createRandomList():
    randomList = []
    n = 8
    for i in range(n):
        randomList.append(rd.randint(1, 10000))
    return randomList

def sortList():
    randomList = createRandomList()
    randomList.sort()
    return randomList

print(createRandomList())
print(sortList())
