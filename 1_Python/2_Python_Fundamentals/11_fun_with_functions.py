# Odd/Even:
# Create a function called odd_even that counts from 1 to 2000.
# As your loop executes have your program print the number of that
# iteration and specify whether it's an odd or even number.

def odd_even():
    for i in range(1, 2000 + 1):
        if i % 2 == 0:
            print "Number is " + str(i) + ". This is an even number."
        else:
            print "Number is " + str(i) + ". This is an odd number."

odd_even()

# Multiply:
# Create a function called 'multiply' that iterates through each value in a list
# (e.g. a = [2, 4, 10, 16]) and returns a list where each value has been multiplied by 5.
# The function should multiply each value in the list by the second argument.


def multiply(arr,num):
    for x in range(0, len(arr)):
        arr[x] *= num
    return arr
a = [2,4,5]
print a
b = multiply(a,3)
print b


# Hacker Challenge:
# Write a function that takes the multiply function call as an argument. 
# Your new function should return the multiplied list as a two-dimensional list.
# Each internal list should contain the number of 1's as the number in the original list.


# arr = [6,12,15]
def layered_multiples(arr):
    new_array = []
    for data in arr:
        sub_array = []
        for i in range(0,data):
            sub_array.append(1)
            
        new_array.append(sub_array)  


    return new_array
x = layered_multiples(multiply([2,4,5],3))
print x


