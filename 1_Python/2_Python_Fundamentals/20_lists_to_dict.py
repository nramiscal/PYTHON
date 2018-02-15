# 070517 nramiscal@gmail.com

# Assignment: Making Dictionaries
# Create a function that takes in two lists and creates a single dictionary where 
# the first list contains keys and the second values. Assume the lists will be of equal length.

# Your first function will take in two lists containing some strings. 
# Here are two example lists:

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(arr1, arr2):
    new_dict = {}
    if len(arr1) == len(arr2):
        new_dict = {}
        for i in range(0, len(arr1)):
            x = "\"" + str(arr1[i]) + "\""
            y = "\"" + str(arr2[i]) + "\""
            new_dict[x] = y

    return new_dict

print make_dict(name, favorite_animal)