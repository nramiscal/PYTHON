for x in range(1,9):
    if x % 2 == 1:
        str = ""
        for y in range(1,9):
            if y % 2 == 1:
                str += "*"
            else:
                str += " "
        print str
    else:
        str = " "
        for y in range(2,9):
            if y % 2 == 0:
                str += "*"
            else:
                str += " "
        print str
            