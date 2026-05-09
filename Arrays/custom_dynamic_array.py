import ctypes


class DynamicArray:

    def __init__(self):
        self.size = 1
        self.items = 0
        self.array = self.__make_array(self.size)

    def __make_array(self, capacity):
        return (capacity * ctypes.py_object)()

    def __len__(self):
        return self.items

    def __str__(self):
        return '[' + ', '.join(
            str(self.array[i]) for i in range(self.items)
        ) + ']'

    def __resize(self, new_capacity):

        new_array = self.__make_array(new_capacity)

        for i in range(self.items):
            new_array[i] = self.array[i]

        self.array = new_array
        self.size = new_capacity

    def append(self, item):

        if self.items == self.size:
            self.__resize(self.size * 2)

        self.array[self.items] = item
        self.items += 1

    def pop(self):

        if self.items == 0:
            raise IndexError('pop from empty list')

        value = self.array[self.items - 1]
        self.items -= 1

        return value

    def clear(self):

        self.size = 1
        self.items = 0
        self.array = self.__make_array(self.size)

    def find(self, item):

        for i in range(self.items):

            if self.array[i] == item:
                return i

        return -1

    def insert(self, pos, item):

        if pos < 0:
            pos += self.items

        if pos < 0 or pos > self.items:
            raise IndexError('list index out of range')

        if self.items == self.size:
            self.__resize(self.size * 2)

        for i in range(self.items, pos, -1):
            self.array[i] = self.array[i - 1]

        self.array[pos] = item
        self.items += 1

    def __delitem__(self, pos):

        if pos < 0:
            pos += self.items

        if pos < 0 or pos >= self.items:
            raise IndexError('list index out of range')

        for i in range(pos, self.items - 1):
            self.array[i] = self.array[i + 1]

        self.items -= 1

    def __getitem__(self, index):

        if isinstance(index, slice):

            result = DynamicArray()

            start, stop, step = index.indices(self.items)

            i = start

            while (step > 0 and i < stop) or (
                step < 0 and i > stop
            ):

                result.append(self.array[i])
                i += step

            return result

        if index < 0:
            index += self.items

        if index < 0 or index >= self.items:
            raise IndexError('list index out of range')

        return self.array[index]

    def __setitem__(self, pos, value):

        if pos < 0:
            pos += self.items

        if pos < 0 or pos >= self.items:
            raise IndexError('list index out of range')

        self.array[pos] = value

    def remove(self, item):

        pos = self.find(item)

        if pos == -1:
            raise ValueError(f'{item} not found in list')

        self.__delitem__(pos)

    def sort(self):

        for _ in range(self.items):

            swapped = False

            for i in range(self.items - 1):

                if self.array[i] > self.array[i + 1]:

                    self.array[i], self.array[i + 1] = (
                        self.array[i + 1],
                        self.array[i]
                    )

                    swapped = True

            if not swapped:
                break

    def min(self):

        if self.items == 0:
            raise ValueError('min() arg is an empty sequence')

        min_value = self.array[0]

        for i in range(1, self.items):

            if self.array[i] < min_value:
                min_value = self.array[i]

        return min_value

    def max(self):

        if self.items == 0:
            raise ValueError('max() arg is an empty sequence')

        max_value = self.array[0]

        for i in range(1, self.items):

            if self.array[i] > max_value:
                max_value = self.array[i]

        return max_value

    def sum(self):

        total_sum = 0

        for i in range(self.items):
            total_sum += self.array[i]

        return total_sum

    def extend(self, iterable):

        for element in iterable:

            if self.items == self.size:
                self.__resize(self.size * 2)

            self.array[self.items] = element
            self.items += 1

    def merge(self, other):

        result = DynamicArray()

        for i in range(self.items):
            result.append(self.array[i])

        for item in other:
            result.append(item)

        return result


L = DynamicArray()

L.append(10)
L.append(20)
L.append(30)
L.append(40)

print(L)
print(L.sum())
print(L.min())
print(L.max())