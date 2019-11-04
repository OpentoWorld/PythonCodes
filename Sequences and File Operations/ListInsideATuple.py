tup = ([1, 2, 3], [3, 4, 5], [5, 6, 7])
print(tup)
print(len(tup))
print(tup[0][0:2])

'''Updating tuple'''
tup[0][1] = 90
print(tup)

'''Deleting element in Tuple'''

del (tup[1][2])
print(tup)