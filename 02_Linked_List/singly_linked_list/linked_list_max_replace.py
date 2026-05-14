class Node:
    
    def __init__(self,value):
        self.data = value
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.numberOfNodes = 0

    def max_replace(self, Value):

        current = self.head

        max = current

        while current != None:
            if current.data > max.data:
                max = current
            current = current.next

        max.data = Value


