# Example: Call by value, string or ints
a = 3
b = 5

def sum(x,y):
    x = x+y
    return x

print(sum(a,b))
print(a, b)

# Example: Call by reference, doesn't support string, but does array, etc. 
liste = [1, 23, 44, 6, 51];

def replace(l):
    l[0] = 0; 
    return l

print(replace(liste))
print(liste)