import math

def dreieck(k1):
    def inner1(k2):
        def inner2(h):
            alpha = math.degrees(math.asin(k1 / h))
            beta = math.degrees(math.asin(k2 / h))
            gamma = 90

            # Ausgabe der Winkel
            print(f"Alpha: {alpha:.2f}°")
            print(f"Beta: {beta:.2f}°")
            print(f"Gamma: {gamma:.2f}°")
        
        return inner2
    return inner1

# Test mit den Werten 3, 4 und 5
dreieck(3)(4)(5)
