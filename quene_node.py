#epic new quene node

class quene_node:

#since python doesn't support multiple constructors,
#we will overload it, and for each item in args,
#we will construct it differently.
    def __init__(self, *args):
        #empty constructor
        if args == ():
            self.data = None
            self.prev = None
            self.next = None

        elif len(args) == 1:
            self.data = args[0]
            self.prev = None
            self.next = None

        else:
            self.data = args[0]
            self.prev = args[1]
            self.next = args[2]

    def get_data(self):
        return self.data

    def get_prev(self):
        return self.prev

    def get_next(self):
        return self.next

    def set_data(self, data):
        self.data = data

    def set_prev(self, prev):
        self.prev = prev

    def set_next(self, next):
        self.next = next

    def toString(self):
        return "Node: "+str(self.data)