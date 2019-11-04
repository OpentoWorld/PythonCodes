''' Sorting and Reversing '''
tup = (1, 3, 4, 0)
print(sorted(tup))
print(tup[::-1])

'''  Multiplication and Membership '''
print(len(tup))
print(sorted(tup*2))
print("Java" in tup)

''' Concatenation and Delete '''
tup1 = (1, 2, 3, 4)
tup2 = tup+tup1
print(tup2)
#del(tup1)'''It will show an error'''
print(tup1)