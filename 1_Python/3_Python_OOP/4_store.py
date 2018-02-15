# 070617 nramiscal@gmail.com

# Now, let's build a store to contain our products by making a store class and putting our 
# products into an array.

# Store class:
# Attributes:
#  - products: an array of products objects
#  - location: store address
#  - owner: store owner's name

# Methods:
#  - add_product: add a product to the store's product list
#  - remove_product: should remove a product according to the product name
#  - inventory: print relevant information about each product in the store

# You should be able to test your classes by instantiating new objects of each class 
# and using the outlined methods to demonstrate that they work.

# class Product(object):

#     def __init__(self, price, item_name, weight, brand, cost):
#         self.price = price
#         self.item_name = item_name
#         self.weight = weight
#         self.brand = brand
#         self.cost = cost
#         self.status = "for sale"

class Store(object):
    def __init__(self, products, location, owner):
        self.products = products
        self.location = location
        self.owner = owner
    
    def add_product(self, new_product):
        self.products.append(new_product)

    def remove_product(self, discontinued):
        for product in self.products:
            if product == discontinued:
                self.products.remove(product)

    def inventory(self):
        print "Inventory:"
        tvs = 0
        wash = 0
        dvd = 0
        for product in self.products:
            if product == "tv":
                tvs += 1
            elif product == "washing machine":
                wash += 1
            elif product == "dvd player":
                dvd += 1
        print tvs, "tv(s)"
        print wash, "washing machine(s)"
        print dvd, "dvd player(s)"


    def display_info(self):
        print self.products
        # print self.location
        # print self.owner


if __name__ == "__main__":
    store1 = Store(["dvd player", "tv"], "2401 Lellah Court, Vienna, VA 22182", "Abby the Malshi")
    store1.display_info()
    store1.add_product("washing machine")
    store1.display_info()
    store1.remove_product("tv")
    store1.display_info()
    store1.inventory()