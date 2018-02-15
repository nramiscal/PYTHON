# 070517 nramiscal@gmail.com

# Assignment: Making Dictionaries
# Hacker Challenge
# If the lists are of unequal length, the longer list should be used for the keys, 
# the shorter for the values.


name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"] #, "dinosaurs", "kittens"]

def make_dict(arr1, arr2):
    new_dict = {}
    if len(arr2) > len(arr1):
        diff = len(arr2) - len(arr1)
        for i in range(0, diff):
            arr1.append("undefined")
        # print arr1
        temp = arr1
        arr1 = arr2
        arr2 = temp
    elif len(arr1) > len(arr2):
        diff = len(arr1) - len(arr2)
        for i in range(0, diff):
            arr2.append("undefined")
        print arr2


    new_dict = {}
    for i in range(0, len(arr1)):
        x = "\"" + str(arr1[i]) + "\""
        y = "\"" + str(arr2[i]) + "\""
        new_dict[x] = y
  


    return new_dict

print make_dict(name, favorite_animal)