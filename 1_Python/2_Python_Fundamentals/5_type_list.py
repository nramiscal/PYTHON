
l1 = ['magical unicorns',19,'hello',98.98,'world']
l2 = [2,3,1,7,4,12]
l3 = ['magical','unicorns']
l4 = [1.2,2.3,3.4,4.5,5.6]
l5 = [1,2.3,4,5.6] 


strcount = 0
strsum = ""
numcount = 0
sum = 0
intcount = 0
fcount = 0

test = l5
print test
for element in test:
    x = type(element)
    if x == str:
        strcount += 1 
        strsum = strsum + " " + element
    elif x == int or x == float:
        numcount += 1
        sum += element
        if x == int:
            intcount += 1
        elif x == float:
            fcount += 1   
    else:
        print "elements in array must be of type str, int or float"

if strcount > 0 and numcount > 0:
    print "The array you entered is of mixed type."
    print "String:", strsum
    print "Sum:", sum
elif strcount == len(test):
    print "The array you entered is of string type."
    print "String:", strsum
elif numcount == len(test) and intcount > 0 and fcount > 0:
    print "The array you entered is of mixed numeric type."
    print "Sum:", sum
elif intcount == len(test):
    print "The array you entered is of integer type."
    print "Sum:", sum
elif fcount == len(test):
    print "The array you entered is of float type."
    print "Sum:", sum


