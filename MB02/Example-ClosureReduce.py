# Modul 323-sw2: Beispiel reduce
from functools import reduce 

def mult(x,y):
    print("x=",x," y=",y)
    return x*y

n = 6
fact = reduce(mult, range(1, n))
print('Factorial of {}: {}'.format(n - 1, fact))