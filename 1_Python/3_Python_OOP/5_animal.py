# 070617 nramiscal@gmail.com

class Animal(object):
    def __init__(self, name):
        self.name = name
        self.health = 100
    def walk(self):
        print "Walking..."
        self.health -= 1
        return self
    def run(self):
        print "Running..."
        self.health -= 5
        return self
    def display_health(self):
        print "Health: " + str(self.health)
        return self
    

animal1 = Animal("Bob")
animal1.display_health().walk().walk().walk().run().run().display_health()

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health = 150
    def pet(self):
        print "Being petted..."
        self.health += 5
        return self


dog1 = Dog("Abby")
super(Dog, dog1).display_health()
super(Dog, dog1).walk().walk().walk().run().run().pet()
super(Dog, dog1).display_health()


class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170
    
    def fly(self):
        print "Flying..."
        self.health -= 10
        return self
    def display_health(self):
        print "I am a dragon."
        super(Dragon, self).display_health()
        return self
        
dragon1 = Dragon("Lenny")
dragon1.display_health()
dragon1.fly().fly().fly()
dragon1.display_health()

animal2 = Animal("Mr. Ed")
# animal2.pet() #do not work because cannot inherit from child class
# animal2.fly()

# dog1.fly() #does not work because cannot inherit from sibling class