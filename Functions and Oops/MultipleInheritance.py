class first(object):
    def __init__(self):
        super(first, self).__init__()
        print("first")


class second(object):
    def __init__(self):
        super(second, self).__init__()
        print("second")



class third(second, first):
    def __init__(self):
        super(third, self).__init__()
        print("third")

third()