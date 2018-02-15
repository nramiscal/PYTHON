# 070517 nramiscal@gmail.com

# Assignment: Stars
# Write the following functions.

# Part I
# Create a function called draw_stars() that takes a list of numbers and prints out *.

x = [4, 6, 1, 3, 5, 7, 25]

def draw_stars(arr):
    for value in arr:
        star_string = ""
        for i in range(0, value):
            star_string += "*"
            # print "*"
        print star_string


draw_stars(x)