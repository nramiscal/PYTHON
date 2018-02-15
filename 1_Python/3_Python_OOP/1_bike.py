class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayInfo(self):
        print "Price: $" + str(self.price)
        print "Max Speed: " + str(self.max_speed) + " mph"
        print "Total miles: " + str(self.miles) + " miles"
        return self
    def ride(self):
        print "Riding..."
        self.miles += 10
        return self
    def reverse(self):
        print "Reversing..."
        self.miles -= 5
        if self.miles < 0:
            self.miles = 0
        return self





bike1 = Bike(200, 25)
bike2 = Bike(300, 50)
bike3 = Bike(1000, 100)

# for i in range(1, 4):
#     bike1.ride()
# bike1.reverse()
# bike1.displayInfo()

bike1.ride().ride().ride().reverse().displayInfo()

# for i in range(1, 3):
#     bike2.ride()
# for i in range(1, 3):
#     bike2.reverse()
# bike2.displayInfo()

bike2.ride().ride().reverse().reverse().displayInfo()

# for i in range(1, 4):
#     bike3.reverse()
# bike3.displayInfo()

bike3.reverse().reverse().reverse().displayInfo()