class Parent:
    def myMethod(self):
        print("Calling Parent method")
class Child(Parent):
    def myMethod(self):
        print("Calling Child method")


x=Child()
x.myMethod()