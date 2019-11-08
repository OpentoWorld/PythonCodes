class AccessSpecifiers():
    def __init__(self):
        self.__pri = ("I am private!!")
        self._pro = ("I am protected!!")
        self.pub = ("I am public!!")


ob = AccessSpecifiers()
print (ob.pub)
print (ob._pro)
#print (ob.__pri)


'''Another program'''
class MyClass:
    def myPublicMethod(self):
        print ('Public Method')
    def __myPrivateMethod(self):
        print ('Private Method')


obj = MyClass()
obj.myPublicMethod()
#obj.__myPrivateMethod()
obj._MyClass__myPrivateMethod()