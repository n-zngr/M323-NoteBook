from functools import reduce
import random as rd

liste = []
for l in range(10):
    liste.append(rd.randint(1,10000))

restList = []
sortList = []

def kleiner(a,b):
    restList.append(b) if a > b else restList.append(a)
    return a if a > b else b

while liste:
    sortList.append(reduce(kleiner,liste))
    liste = restList
    print("rest list:" + str(restList))
    restList = []
    print("sorted list:" + str(sortList))

print(sortList)