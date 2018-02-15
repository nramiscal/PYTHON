# 070517 nramiscal@gmail.com

# Assignment: Making and Reading from Dictionaries
# Create a dictionary containing some information about yourself.
# The keys should include name, age, country of birth, favorite language.
# Write a function that will print something like the following as it executes:

# My name is Anna
# My age is 101
# My country of birth is The United States
# My favorite language is Python

profile = {"name": "Anna", "age": "101", "country of birth": "The United States", "favorite language": "Python"}


def display_profile(d):
    for key, data in profile.iteritems():
        print "My", key, "is", data

display_profile(profile)