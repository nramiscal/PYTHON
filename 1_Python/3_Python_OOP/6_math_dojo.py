# 070617 nramiscal@gmail.com

class MathDojo(object):
    def __init__(self, num):
        self.result = num
        
    def add(self, *t):   
        # print t
        for i in range(0, len(t)):
            if type(t[i]) == list:
                for item in t[i]:
                    self.result += item
                # print self.result
            elif type(t[i]) == int:
                self.result += t[i]
        # print self.result
        return self

    def subtract(self, *t):
        for i in range(0, len(t)):
            if type(t[i]) == list:
                for item in t[i]:
                    self.result -= item
            elif type(t[i]) == int:
                self.result -= t[i]
        
        
        return self


print MathDojo(0).add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result
print MathDojo(0).add(2).add(2, 5).subtract(3, 2).result


