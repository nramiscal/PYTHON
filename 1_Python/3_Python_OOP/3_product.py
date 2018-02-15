# 070617 nramiscal@gmail.com

# The owner of a store wants a program to track products.
# Create a product class to fill the following requirements...



class Product(object):

    def __init__(self, price, item_name, weight, brand, cost):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "for sale"
    
    def sell(self):
        self.status = "sold"
        print "This product was sold"
        return self

    def add_tax(self, tax):
        total_price = self.price * (1 + tax)
        print "Price with tax is $" + str(total_price)
        return total_price
    
    def return_reason(self, reason):
        if reason == "defective":
            self.price = 0
            self.status = "defective"
        elif reason == "returned in the box, like new":
            self.status = "for sale"
        elif reason == "box opened":
            self.status = "used"
            self.price = self.price * 0.8
        return self

    def display_info(self):
        print "Price: $" + str(self.price)
        print "Item Name: " + self.item_name
        print "Weight: " + str(self.weight) + "lbs"
        print "Brand: " + self.brand
        print "Cost: $" + str(self.cost)
        print "Status: " + self.status
        return self


if __name__ == "__main__":
    product1 = Product(50, "DVD Player", 10, "Panasonic", 20)
    # product1.add_tax(0.06)


    # product1.display_info()
    # product1.sell()
    # product1.display_info()

    product2 = Product(80, "TV", 30, "Sony", 40)
    product2.display_info()
    product2.return_reason("box opened")
    product2.display_info()

    product3 = Product(200, "Washing Machine", 150, "GE", 100)



