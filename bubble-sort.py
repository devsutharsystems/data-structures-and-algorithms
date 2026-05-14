#my_code

def bubbleSort(arr):

    
    for j in range(len(arr)-1):
        swap = 0
        for i in range(len(arr)-1-j):
            if arr[i] > arr[i+1]:
                arr[i+1],arr[i] = arr[i],arr[i+1]
                swap += 1

        if swap == 0:
            break
            
        return arr


arr = [0, 2, 5, 3, 6, 1, 8]
print(bubbleSort(arr))
