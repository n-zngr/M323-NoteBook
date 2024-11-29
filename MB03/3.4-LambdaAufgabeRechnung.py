def divZeroab(a,b): 
    if (a != 0 | b != 0): 
        return a/b
    else: 
        return "Can't execute, as one of the numbers are equal to 0"

print(divZeroab(0,2))

y= (lambda x,y: x/y) (5,2)
print(y)

z= ((lambda x,y: x/y if y != 0 else None) (5,2))
print(z)