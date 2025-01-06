def compose (a, b): 
    def c(x):
        return a(b(x))
    return c

def d(x):
    return x*x*x

def e(x):
    return 2*x+1

calculate = compose(d,e)

x = list(range(1, 19))
fx = list(map(calculate, x))
dx = list(map(d,x))
ex = list(map(e, x))

print(x)
print(fx)
print(dx)
print(ex)