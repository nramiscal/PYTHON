# 070617 nramiscal@gmail.com

from datetime import datetime


class Call(object):
    def __init__(self, name, phone, reason):
        self.id = id(self)
        self.name = name
        self.phone = phone
        self.time = datetime.now()
        self.reason = reason


    def display_info(self):
        print "ID: #" + self.id
        print "Caller name: " + self.name
        print "Caller phone number: " + self.phone
        print "Time of call: " + self.time
        print "Reason for call: " + self.reason

    def __str__(self):
        return "Call #{} from {} ({}) for '{}' at {}".format(self.id, self.name, self.phone, self.reason, self.time)

# call1 = Call("Abby", "867-5309", "order status")
# print call1


class Call_Center(object):
    def __init__(self):
        self.calls = []
    def add(self, name, phone, reason):
        new_call = Call(name, phone, reason)
        self.calls.append(new_call)
        self.queue_size = len(self.calls)
        print new_call
        print self.queue_size
    def remove(self):
        self.calls.remove(self.calls[0])
        self.queue_size = len(self.calls)
        print "Removing call"
    def info(self):
        print "the queue size is {}:".format(self.queue_size)
        for call in self.calls:
            print call
        return self
    def removeByNumber(self, phone):
        for call in self.calls:
            if call.phone == phone:
                self.calls.remove(call)
            self.queue_size = len(self.calls)
        return self
            
                



center1 = Call_Center()
center1.add("Abby", "867-5309", "order status")
center1.add("Joan", "123-4567", "change of address")
center1.add("Waldo", "432-6553", "cannot complete order")
center1.info()
center1.removeByNumber("123-4567")
center1.info()



















# call2 = Call("abc", "Joan", "123-4567", "9:30 pm", "change of address")
# call3 = Call("789", "Waldo", "432-6553", "12 pm", "cannot complete order")

# my_list = [call1, call2]

# call1.display_info()

# class Call_Center(Call):
#     def __init__(self):
#         super(Call_Center, self).__init__(self, id, name, phone, time, reason):)
#         self.calls = []
#         self.queue = len(self.calls)

#     def add(self):
#         x = super(Call_Center, self).__init__(self)
#         self.calls.append(x)
#         print self.calls


# cc1 = Call_Center("xyz", "Tallulah", "867-5309", "7:30 am", "order status")
# print cc1
# super(Call_Center, cc1).display_info()
# cc1.add()

