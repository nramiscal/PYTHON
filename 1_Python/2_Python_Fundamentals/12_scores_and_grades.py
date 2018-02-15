# 070517 nramiscal@gmail.com

# Write a function that generates ten scores between 60 and 100. 
# Each time a score is generated, your function should display what 
# the grade is for a particular score. Here is the grade table:

# Score: 60 - 69; Grade - D
# Score: 70 - 79; Grade - C
# Score: 80 - 89; Grade - B
# Score: 90 - 100; Grade - A


import random

def generate_score():
    r = int(random.random() * 40 + 60)
    return r


print "Scores and Grades"
for i in range(0,10):
    score = generate_score()
    if score < 70:
        print "Score:" + str(score) + "; Your grade is D"
    elif score < 80:
        print "Score:" + str(score) + "; Your grade is C"
    elif score < 90:
        print "Score:" + str(score) + "; Your grade is B"
    else:
        print "Score:" + str(score) + "; Your grade is A"
print "End of the program. Bye!"