def quadratzahlen_positiv(liste):
    return list(map(lambda x: x**2, filter(lambda x: x > 0, liste)))

testliste = [-3, -5, -10, 12, 6, 5, -30]

ergebnis = quadratzahlen_positiv(testliste)
print(ergebnis)
