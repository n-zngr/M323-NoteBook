import math


def curry(func): 
    def inner(arg): 
        if len(signature(func).parameters) == 1:
            return func(arg)
    return curry()

# curry kapselt den block und löst die Funktion über die allgemein formulierte Funktion curry
@curry
def nullstellen (a,b,c):
    if b * b < 4 * a * c:
        return None
    x1 = (-b + math.sqrt((b*b) - (4 * a * c))) / 4 * a
    x2 = (-b + math.sqrt((b*b) - (4 * a * c))) / 4 * a
    return x1, x2

nullstellenres = nullstellen(2)(0)(10)

print('Nullstellen: x1: 0', nullstellenres[0], 'x2:', nullstellenres[1])