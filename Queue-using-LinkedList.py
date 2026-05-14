class Node:
    def __init__(self, value):

        self.data = value
        self.next = None

class Queue:

    def __init__(self):
        self.front = None
        self.rear = None
        self.numberOfNodes = 0

    def enqueue(self, value):
        new_node = Node(value)

        if self.rear == None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        self.numberOfNodes += 1

    def dequeue(self):

        if self.front == None:
            return print('queue is already empty')
        else:
            self.front = self.front.next

        self.numberOfNodes -= 1

    def traverse(self):

        if self.front == None:
            return print('queue is empty')
        else:
            current = self.front
            result = ''
            
            while current != None:
                result = result + str(current.data) + '->'
                current = current.next

            return print(result[:-2])
        
    def is_empty(self):

        return print(self.front == None)
    
    def size(self):

        return print(self.numberOfNodes)
    
    def frontPick(self):
        if self.front == None:
            return print('Empty queue')
        else:
            return print(self.front.data)
    
    def rearPick(self):
        if self.front == None:
            return print('Empty queue')
        else:
            return print(self.rear.data)

        

Q = Queue()

Q.enqueue(1)
Q.enqueue(2)
Q.enqueue(3)
Q.enqueue(4)

Q.dequeue()

Q.frontPick()
Q.rearPick()
Q.is_empty()
Q.size()


Q.traverse()
                
