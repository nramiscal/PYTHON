# 070517 nramiscal@gmail.com

# Part II
# Modify the function above. Allow a list containing integers and strings
# to be passed to the draw_stars() function. When a string is passed,
# instead of displaying *, display the first letter of the string according
# to the example below. You may use the .lower() string method for this part.

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

def draw_stars(arr):
    for value in arr:
        if type(value) == int:
            char = "*"
            display_string = ""
            for i in range(0, value):
                display_string += char
            print display_string
        elif type(value) == str:
            char = value[0].lower()
            display_string = ""
            for i in range(0, len(value)):
                display_string += char
            print display_string
        
        

draw_stars(x)

