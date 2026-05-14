def binarySearch(arr, target):
    low = 0
    high = len(arr)/2

    while low <= high:

        mid = (low + high)//2

        if arr[mid] == target:
            return mid
        
        elif arr[mid] < target:
            low = mid + 1
        
        else:
            high = mid - 1

    return -1

def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True



def monkeySort(arr):
    import random

    counter = 0

    while not is_sorted(arr):
        random.shuffle(arr)
        counter += 1
        print(counter)

    return arr


arr = [0, 1, 2, 4, 3, 5, 6]

print(is_sorted(arr))
monkeySort(arr)
print(is_sorted(arr))

    


