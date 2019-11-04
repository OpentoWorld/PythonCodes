
#Indexing and Slicing
list = ["Hadoop", "Python", "Android"]
print(list[1])
print(list[0:2])
print(list[-1])

#Updating and Deleting Elements
list[1] = "Java"
print(list)
del(list[2])
print(list)

#Remove and Pop functions
list1 = ['1', '2', '3', '4', '5', 'a', 'b', 'c']
print(list1.pop(3))
list1.remove('a')
print(list1)

#Type
print(type(list1))
