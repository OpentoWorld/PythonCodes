class variable:
    domain = ("Data Science")
    def setCourse(self,name):
        self.name = name


ob1 = variable()
ob2 = variable()

ob1.setCourse("Python")
ob2.setCourse("Machine Learning")
print (ob1.domain)

ob1.domain = 'GOD'
print (ob1.domain)

print(ob2.domain)