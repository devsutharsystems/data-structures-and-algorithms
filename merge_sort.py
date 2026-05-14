def merge_sorted(arr1, arr2, arr):
    i = j = k = 0


    while i < len(arr1) and j < len(arr2):

        if arr1[i] < arr2[j]:
            arr[k] = arr1[i]
            i+=1
        else:
            arr[k] = arr2[j]
            j+=1
        k+=1

    while i<len(arr1):
        arr[k] = arr1[i]
        i+=1
        k+=1


    while j<len(arr2):
        arr[k] = arr2[j]
        j+=1
        k+=1

    return arr

def merge_sort(arr):

    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge_sorted(left, right, arr)


arr = [8,7,6,2,3,5,4,1,0]
print(merge_sort(arr))
