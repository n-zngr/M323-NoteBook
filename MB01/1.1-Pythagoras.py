import math;

a = 4;
b = 3;

def Pythagoras(a, b): 
    c = math.sqrt(a**2 + b**2)

    return c
    
print(Pythagoras(a, b))



def quadrat(kat): 
    return kat*kat;

def hypothenuse(kat1, kat2):
    hypothenuse = math.sqrt(quadrat(kat1) + quadrat(kat1))

    return hypothenuse

print("Hypothenuse der zweite Katheten betraegt:", PythagorasHypothenuse(6,8))