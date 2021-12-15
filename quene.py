#main class for quene
class quene:

    #empty constructor
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    #enquene method, if length is 0, then it
    #runs differently
    def enquene(self, element):
        if self.length == 0:
            self.first = element
            self.last = element

        else:
            self.last.set_next(element)
            element.set_prev(self.last)
            self.last = element

        self.length+=1

    #if there is more than 1 node, it will
    #set the second node to the first and
    #return the previous top node. If there
    #is only one node, it will remove and return it
    def dequene(self):
        try:
            self.first.get_next().set_prev(None)
            temp = self.first
            self.first = self.first.get_next()
            self.length-=1
            return temp
        except:
            temp = self.first
            self.first = None
            return temp

    #returns boolen, is empty
    def isEmpty(self):
        return self.length==0

    #returns size (self.length)
    def size(self):
        return self.length

    #returns the top node without
    #removing it
    def peek(self):
        return self.first