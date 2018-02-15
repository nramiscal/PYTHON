# 070517 nramiscal@gmail.com

# Names, Part II
# Create a program that prints the following format (including number of characters in each combined name):

# Students
# 1 - MICHAEL JORDAN - 13
# 2 - JOHN ROSALES - 11
# 3 - MARK GUILLEN - 11
# 4 - KB TONEL - 7
# Instructors
# 1 - MICHAEL CHOI - 11
# 2 - MARTIN PURYEAR - 13


users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def num_chars(str1, str2):
    sum = 0
    for c in str1+str2:
        sum += 1
    return sum


def school_info(d):
    for key, data in d.items():
        count = 0
        print key
        for value in data:
            count += 1
            print count, "-", value["first_name"].upper(), value["last_name"].upper(), "-", num_chars(value["first_name"], value["last_name"])


school_info(users)