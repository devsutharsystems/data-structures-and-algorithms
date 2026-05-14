import ctypes

class MeraList:
    def __init__(self):
        self.size = 1
        self.items = 0
        self.array = self.__make_array(self.size)

    def __make_array(self,capacity):
        return(capacity*ctypes.py_object)()
    
    def __len__(self):
        return self.items
    
    def __str__(self):
        result = ''
        for item in range(self.items):
            result = result + str(self.array[item]) + ','

        return '[' + result[:-1] + ']'
     
    def append(self,item):
        if self.items == self.size:
            #resize
            self.__resize(self.size*2)
            #add item
            self.array[self.items] = item
            self.items = self.items + 1
        else:
            self.array[self.items] = item
            self.items = self.items + 1

    def __resize(self,new_capacity):
        # create a new array
        new_array = self.__make_array(new_capacity)
        self.size = new_capacity
        # copy the content
        for index in range(self.items):
            new_array[index] = self.array[index]
        # reassign A
        self.array = new_array

 
    def __getitem__(self, index):
        if 0 <= index < self.items:
            return self.array[index]
        else:
            return 'IndexError: Index out of range.'
        
    def pop(self):
        if self.items > 0:
            print(self.array[self.items-1])
            self.items = self.items - 1
        else:
            return 'List already empty.'
        
    def clear(self):
        if self.items == 0:
            return 'List already empty!'
        else:
            self.items = 0
            self.size = 1

    def find(self, number):
        for i in range(self.items):
            if self.array[i] == number:
                return i

        print('item not found')

    def insert(self, pos, number):
        if self.items == self.size:
            self.__resize(self.size*2)

        for i in range(self.items, pos, -1):
            self.array[i] = self.array[i-1]

        self.array[pos] = number
        self.items = self.items + 1

    def __delitem__(self, pos):
        if 0 <= pos < self.items:
            for i in range(pos, self.items - 1):
                    self.array[i] = self.array[i+1]

            self.items = self.items - 1
        
        else:
            return 'IndexError: Index out of range.'

    def remove(self, item):
        pos = self.find(item)

        if type(pos) == int:
            self.__delitem__(pos)
        else:
            return pos
        

    def sort(self):
        for _ in range(self.items):
            swapped = False
            for i in range(self.items - 1):
                if self.array[i] > self.array[i + 1]:
                    self.array[i], self.array[i + 1] = self.array[i + 1], self.array[i]
                    swapped = True
            if not swapped:
                break

    def min(self):

        if self.items == 0:
            return 'List is empty.'
        

        min_value = self.array[0]

        for i in range(self.items - 1):
            if self.array[i] < min_value:
                min_value = self.array[i]

        return print(min_value)

    def merge(self, other):
        result = MeraList()

        for i in range(self.items):
            result.append(self.array[i])

        for item in other:
            result.append(item)

        return result
    
    def max(self):
        
        if self.items == 0:
            return 'List is empty.'
        
        max_value = self.array[0]

        for i in range(self.items - 1):
            if self.array[i] > max_value:
                max_value = self.array[i]

        return print(max_value)
    
    def sum(self):

        for i in range(self.items - 1):
            total_sum = self.array[i] + self.array[i+1]
        return print(total_sum)

    def extend(self, iterable):
        for element in iterable:
            if self.item == self.size:
                self.__resize(self.size * 2)

            self.array[self.items] = element
            self.items += 1

    def __getitem__(self, index):

        if isinstance(index, slice):


            result = MeraList()

            start, stop, step = index.indices(self.items)

            i = start
            while (step > 0 and i < stop) or (step < 0 and i > stop):
                result.append(self.array[i])

                i += step

            return result
        

        if index < 0:
            index = index + self.items

        if index < 0 or index >= self.items:
            raise IndexError('Index out of range')
        
        return self.array[index]






L = MeraList()

L.append(0)
L.append(1)
L.append(3)
L.append(2)

print(L)

L.sum()
