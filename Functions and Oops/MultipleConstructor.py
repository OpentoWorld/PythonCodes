class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        #print(init)
    @classmethod
    def dmy(cls, day, month, year):
        cls.year = year
        cls.month = month
        cls.day = day
        return cls(cls.year, cls.month, cls.day)
    @classmethod
    def mdy(cls, month, day, year):
        cls.year = year
        cls.month = month
        cls.day = day
        return cls(cls.year, cls.month, cls.day)


a = Date(2017, 5, 11)
print ("Year=", a.year)
print ("Month=", a.month)
print ("Day=", a.day)

b = Date(11, 5, 2019)
print ("Year=", b.year)
print ("Month=", b.month)
print ("Day=", b.day)