def info(name, age = 50):
    print("Name=", name)
    print("Age=", age)

info("rakesh")  #  Default age will be displayed
info("Deepa", 34)


'''Another example'''

def employee(name, id, salary = 10000):
    print("Name of employee", name)
    print("Id of employee", id)
    print("Salary of employee", salary)


employee("rakesh", 21)
employee("Dinesh", 32, 20000)