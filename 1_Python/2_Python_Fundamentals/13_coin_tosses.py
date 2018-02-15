# 070517 nramiscal@gmail.com

# Write a function that simulates tossing a coin 5,000 times. 
# Your function should print how many times the head/tail appears.

import random

def coin_toss(reps):
    heads = 0
    tails = 0
    print "Starting the program..."
    for i in range (1, reps + 1):
        outcome = round(random.random())
        if outcome == 0:
            heads += 1
            print "Attempt #" + str(i) + ": Throwing a coin... It's a head! ... Got " + str(heads) + " head(s) so far and " + str(tails) + " tail(s) so far"
        else:
            tails += 1
            print "Attempt #" + str(i) + ": Throwing a coin... It's a tail! ... Got " + str(tails) + " tail(s) so far and " + str(heads) + " head(s) so far"
    print "Ending the program, thank you!"

coin_toss(5000)