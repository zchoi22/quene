
class quene:

    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def enquene(self, element):
        if self.length == 0:
            self.first = element
            self.last = element

        else:
            self.last.set_next(element)
            element.set_prev(self.last)
            self.last = element

        self.length+=1

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

    def isEmpty(self):
        return self.length==0

    def size(self):
        return self.length

    def peek(self):
        return self.first