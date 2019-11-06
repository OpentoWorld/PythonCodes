a = 50  # Global variable
def number():
    b = 10  # Local variable
    print(b)

print(a)
number()



'''Another example'''

a = 30
def add(b):
    c = 30
    print("c=",c)
    sum = b+c
    print(sum)
print(a)
add(40)
print(b)
'''It will show error because b is declared locally in the program'''