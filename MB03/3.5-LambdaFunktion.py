list = [-3, -2, -1, 0, 1, 2, 3]

z = (lambda lst: lst.sort(reverse=True) or lst)(list)

print(z)

