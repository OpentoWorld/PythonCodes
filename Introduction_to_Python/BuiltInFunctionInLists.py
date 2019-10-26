list = [1, 2, 3]

list.append('Machine language')
print(list)
list.extend(['g','h'])
print(list)
list.insert(1, 'Scripting')
print(list)
list.remove(3)
print(list)
list.remove('Machine language')
print(list)

list1 = ['Java', 'Python', 'C++']
print(sorted(list1))