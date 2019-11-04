import os

newfile = open("Edureka_py.txt", "w+")
for i in range(1, 10):
    newfile.write("\n Hello, Welcome to Python")
for i in range (1, 10):
    print(newfile.read())

newfile1 = open("Edureka.txt", "r")
newfile.seek(0)
print(newfile.tell())
os.rename("Edureka.txt", "Python.txt")
os.remove("Edureka.txt")
newfile.close()