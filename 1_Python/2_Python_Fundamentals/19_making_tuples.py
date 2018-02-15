# 070517 nramiscal@gmail.com

# Dictionary In, Tuples Out
# Write a function that takes in a dictionary and returns a list of tuples 
# where the first tuple item is the key and the second is the value. Here's an example:

# # function input
# my_dict = {
#   "Speros": "(555) 555-5555",
#   "Michael": "(999) 999-9999",
#   "Jay": "(777) 777-7777"
# }
# #function output
# [("Speros", "(555) 555-5555"), ("Michael", "(999) 999-9999"), ("Jay", "(777) 777-7777")]

my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}


def make_tuples(d):
    arr = []
    for key, data in d.iteritems():
        t = (key, data)
        arr.append(t)
    print arr
    return arr


make_tuples(my_dict)  