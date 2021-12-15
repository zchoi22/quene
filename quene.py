from quene_node import quene_node as qn

class quene:

    def __int__(self):
        self.first = None
        self.last = None
        self.size = 0

    def enquene(self, element):
        if self.size == 0:
            self.first = element
            self.last = element

        else:
            self.last.set_next(element)
            element.set_prev(self.last)
            self.last = element

    def dequene(self):
        self.first.get_next().set_prev(None)
        temp = self.first
        self.first = self.first.get_next()
        return temp

    def isEmpty(self):
        return self.size==0

    def size(self):
        return self.size

    def peek(self):
        return self.first