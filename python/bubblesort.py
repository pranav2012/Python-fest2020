def bubblesort(arr):
    swap_happened = True
    count = 0
    while swap_happened:
        print('sort status',count,str(arr))
        swap_happened = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i+1]:
                swap_happened = True
                arr[i],arr[i+1] = arr[i+1],arr[i]
        count += 1
    return arr

l = [6,4,535,2,24,12,1,3,55,4545]
print('unsorted list is',l)
print('sorted list is',bubblesort(l))