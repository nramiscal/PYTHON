word_list = ['hello','world','my','name','is','Nina']
word_list = ["good","morning", "sunshine", "have", "a", "wonderful", "day"]
char = "n"

new_list = []
for element in word_list:
    # print element
    for c in element:
        if c == char:
            # print element
            new_list.append(element)
            break
print "new_list =", new_list