class GetterAndSetter:
    def __init__(self, courseName):
        self.courseName = courseName

    def setCourseName(self, courseName):
        self.courseName = courseName

    def getCourseName(self):
        print(self.courseName)



x = GetterAndSetter("Python")
x.getCourseName()

x.setCourseName("Machine Learning")
x.getCourseName()