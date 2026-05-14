class Node:

    def __init__(self,value):
        self.data = value
        self.next = None

class LinkedList:

    def __init__(self):

        #EMPTY LINKEDLIST CREATION

        # first node
        self.head = None

        #number of nodes in the LinkedList
        self.numberOfNodes = 0

    def __len__(self):
        return self.numberOfNodes
    
    def insert_head(self, value):

        #making new_node
        new_node = Node(value)

        # connecting new_node's tail to first node head
        new_node.next = self.head

        #making new_node first node of the linkedlist
        self.head = new_node

        #increase count of number of nodes by 1
        self.numberOfNodes += 1

    def __str__(self):
        
        curr = self.head

        result = ''

        while curr != None:
            result = result + str(curr.data) + '->'
            curr = curr.next
            
        return result[:-2]
    
    def push(self, value):

        #creation of new_node
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
            self.numberOfNodes += 1
            return

 
        current = self.head

        while current.next != None:
            current = current.next

        current.next = new_node
        self.numberOfNodes += 1

    
    def insert_after(self, after, value):

        #creation of new_node
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
            self.numberOfNodes += 1
            return

        current = self.head

        while current != None and current.data != after:
            current = current.next

        
        if current != None:
            new_node.next = current.next
            current.next = new_node
            self.numberOfNodes += 1
        else:
            return print('Item not found')
        
    def clear(self):
        self.head = None
        self.numberOfNodes = 0
  

    def pop(self):

        current = self.head

        if current == None:
            return print('List already empty')
        
        elif current.next == None:
            self.head = None
            self.numberOfNodes -= 1

        else:
            while current.next.next != None:
                current = current.next
                
            current.next = None
            self.numberOfNodes -= 1

    def remove(self, value):

        current = self.head

        if current == None:
            return print('List already empty')

        elif current.data == value:
            self.delete_head()

        else:
            while current.next.data != value:
                current = current.next

            if current.next.next == None:
                current.next = None

            else:
            
                current.next = current.next.next
                current.next.next == None
                self.numberOfNodes -= 1

    def search(self, value):

        current = self.head

        if current == None:
            return print('No value in the list')
        
        else:
            index = 0
            while current != None and current.data != value:
                current = current.next
                index += 1

        if 0 <= index <= self.numberOfNodes-1:
            print(index)
        else:
            print('Item not in list')

        
    def __getitem__(self, index):

        current = self.head

        pos = 0

        if current == None:
            return print('No value in the list')
        
        else:
            while current != None:
                if pos == index:
                    return print(current.data)
                current = current.next
                pos += 1

    
            return print('index out of range')
        
    def max_replace(self, Value):

        current = self.head

        max = current

        while current != None:
            if current.data > max.data:
                max = current
            current = current.next

        max.data = Value

    def sum_oddindex(self):

        current = self.head
        counter = 0
        result = 0

        while current != None:
             
             if counter % 2 != 0:
                result = result + current.data

             counter += 1
             current = current.next

        return (print(result))
    
    # reverse by making new liskedlist
    
    def reverse_new(self):
        
        current = self.head

        numbers = []

        while current != None:
            numbers.append(current.data)
            current = current.next
    
        for number in numbers[::-1]:
            self.push(number)

    
    # reverse pre existing liskedlist
    
    def reverse_existing(self):

        previous = None
        current = self.head

        while current != None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
            
        previous = self.head





        

L = LinkedList()

L.insert_head(0)
L.insert_head(1)
L.insert_head(2)
L.insert_head(3)
L.insert_head(4)

print(L)
L.traverse()


