l1 = [1,2,5,6,2]
l2 = [1,2,5,6,2]

# l1 = [1,2,5,6,5]
# l2 = [1,2,5,6,5,3]

# l1 = [1,2,5,6,5,16]
# l2 = [1,2,5,6,5]

# l1 = ['celery','carrots','bread','milk']
# l2 = ['celery','carrots','bread','cream']

print "l1: ", l1
print "l2: ", l2
if len(l1) != len(l2):
    print "The lists are not the same."
else:
    i = 0
    for element in l1:
        if element != l2[i]:
            print "The lists are not the same"
            break
        i += 1
    else:
        print "The lists are the same."    
        