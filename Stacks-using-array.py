class Stack:

    def __init__(self,size):
        self.size = size
        self.stack = [None] * self.size
        self.top = -1

    def push(self, value):

        if self.top == self.size - 1:
            return print("Overflow")
        else:
            self.top += 1
            self.stack[self.top] = value

    def pop(self):

        if self.top == -1:
            return print("Underflow")
        else:
            data = self.top
            self.top -= 1
            return print(data)
        
    def traverse(self):

        for values in range(self.top + 1):
            print(self.stack[values], end="")
            
