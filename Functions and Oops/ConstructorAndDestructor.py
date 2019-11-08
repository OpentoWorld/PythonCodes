class TestClass:
    def __init__(self):
        print ("Contructor")


    def __del__(self):
        print ("Destructor")

if __name__ == "__main__":
    obj = TestClass()
    del obj