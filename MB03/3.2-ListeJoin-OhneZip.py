liste1 = ["Hänsel", "Max", "Susi", "Bonny", "Batman", "Dick"]
liste2 = ["Gretel", "Moritz", "Strolch", "Clide", "Robin", "Doof"]

liste3 = [1,2,3,4,5,6,7,8,9,10]
liste4 = [10,25,5]

def join(a,b):
    return a, b

def mult(a,b):
    return a*b

resultat = list(map(join,liste1,liste2))

print(list(map(mult, liste3, liste4)))

print(resultat)