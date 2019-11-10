class animal:
    def eat(self):
        print("Eating...")


class dog(animal):
    def bark(self):
        print ("Barking...")

class babydog(dog):
    def weep(self):
        print ("Weeping...")

x = babydog()
x.eat()
x.bark()
x.weep()