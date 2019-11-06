lam = lambda z:z+4
print(lam(4))

# Map
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
print(squared)

# Filtered
number = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number))
print(less_than_zero)

# Reduce
from functools import reduce
product = reduce((lambda x, y: x*y), [1, 2, 3, 4])
print(product)