def selectionSort(arr):
    
    for i in range(len(arr) - 1):
        front = i
        min = i
        for mover in range(front + 1, len(arr)):
            if arr[mover] < arr[min]:
                min = mover

        arr[front],arr[min] = arr[min],arr[front]

    return print(arr)
        
                

arr = [1, 3, 4, 2, 6, 9, 8, 5, 0]
selectionSort(arr)
