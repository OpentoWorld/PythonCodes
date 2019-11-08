class base:
    def fun(self):
        print ("First Class!!!")

class sub(base):
    print ("Second Class")
    '''Here sub class will execute first then the base class'''


a = sub()
a.fun()