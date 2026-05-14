class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None




class LinkedList:

    def __init__(self):

        #EMPTY LINKEDLIST CREATION

        # first node
        self.head = None

        #number of nodes in the LinkedList
        self.numberOfNodes = 0

    
    def delete_head(self):

        if self.head == None:
         return print('List already empty')
        
        
        self.head = self.head.next
        self.numberOfNodes -= 1

    
    def __str__(self):
        
        curr = self.head

        while curr != None:
            print(curr.key, "-->", curr.value, " ", end=" ")
            curr = curr.next


    def size(self):
        return self.numberOfNodes
    

    
    def push(self, key, value):

        #creation of new_node
        new_node = Node(key, value)

        if self.head == None:
            self.head = new_node
            self.numberOfNodes += 1
            return

 
        current = self.head

        while current.next != None:
            current = current.next

        current.next = new_node
        self.numberOfNodes += 1





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



    def search(self, key):
        current = self.head
        index = 0

        while current is not None:
            if current.key == key:
                return index
            current = current.next
            index += 1

        return -1

    def get_node_at_index(self,index):

            temp = self.head
            counter = 0

            while temp is not None:

                if counter == index:
                    return temp
                temp = temp.next
                counter += 1


class Dictionary:

    def __init__(self, capacity):

        self.capacity = capacity
        self.size = 0

        self.buckets = self.make_array(self.capacity)

    def make_array(self, capacity):

        L = []

        for _ in range(capacity):
            L.append(LinkedList())

        return L

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)


    def get(self, key):

        bucket_index = self.hash_function(key)

        current = self.buckets[bucket_index].head

        
        while current != None:
            if current.key == key:
                return current.value
            current = current.next

        return None


    def __str__(self):

        result = ""

        for i in range(self.capacity):
            result += f"Bucket {i}: "

            current = self.buckets[i].head

            while current is not None:
                result += f"({current.key} : {current.value}) -> "
                current = current.next

            result += "None\n"

        return result

    
    def put(self, key, value):
        bucket_index = self.hash_function(key)

        node_index = self.get_node_index(bucket_index, key)

        if node_index == -1:
            #insert
            self.buckets[bucket_index].push(key, value)
            self.size += 1

            if self.size/self.capacity >= 0.7:
                self.rehash()
        else:
            #update
            node = self.buckets[bucket_index].get_node_at_index(node_index)
            node.value = value

    def __delitem__(self, key):

        bucket_index = self.hash_function(key)

        removed = self.buckets(bucket_index).remove(key)




    def rehash(self):
        old_capacity = self.capacity
        old_buckets = self.buckets

        self.capacity = self.capacity*2
        self.buckets = self.make_array(self.capacity)

        self.size = 0

        for i in range(old_capacity):

            current = old_buckets[i].head

            while current != None:
                self.put(current.key, current.value)
                current=current.next


    def get_node_index(self, bucket_index, key):
        node_index = self.buckets[bucket_index].search(key)
        return node_index
    

    def hash_function(self, key):
        return abs(hash(key) % self.capacity)

D1 = Dictionary(2)

D1.put("python", 45)
D1.put("python1", 46)
D1.put("python2", 47)
D1.put("python3", 48)
D1.put("python4", 49)
D1.put("python5", 50)
D1.put("python6", 51)
D1.put("python7", 52)
D1.put("python8", 53)
D1.put("python9", 54)
D1.put("python10",54)
D1.put("python11",55)



print(D1["python7"])









