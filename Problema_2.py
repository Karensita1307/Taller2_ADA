class Queue:

    def __init__(self):
        name = input("Ingrese el nombre del paciente: ")
        self.head = 0
        self.tail = -1
        self.e = []

    def enqueue(self,x):
        self.e.append(x)
        self.tail = self.tail + 1

    def dequeue(self):
        if len(self.e) == 0:
            return None
        else:
            v = self.e.pop(0)
            self.tail = self.tail - 1
            return v

    def first(self):
        return self.e[0]

    def last(self):
        return self.e[-1]

    def size(self):
        return len(self.e)

    def isEmpty(self):
        return len(self.e) == 0 


