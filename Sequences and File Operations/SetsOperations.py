s = {1, 2, 3, 4, 5}
set1 = {1, 'a', 'b'}
print(1 in s)
print(set1.issubset(s))
print(s.issuperset(set1))
print(5 not in s)
print(s.union(set1))
print(s.intersection(set1))
print(s.difference(set1))
print(s.symmetric_difference(set1))
s.add('c')
print(s)
s.remove(1)
print(s)
s.pop()
print(s)
s.clear()
print(s)
s.discard()
print(s)