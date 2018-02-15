# 070517 nramiscal@gmail.com

# Assignment: Names

# Create a program that outputs:

# Michael Jordan
# John Rosales
# Mark Guillen
# KB Tonel

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def full_name(l):
    for value in l:
        display_string = ""
        for key, data in value.iteritems():
            display_string += " " + data
        print display_string



full_name(students)
        