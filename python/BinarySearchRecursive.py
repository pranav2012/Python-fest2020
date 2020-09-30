# main code for binary search
def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1

# input list
print("Enter the elements:")
A=list(map(int,input().split()))
print("Enter the element to be searched:")
x=int(input())

result = binary_search(A, 0, len(A)-1, x)
if result != -1:
    print("Element is present at index", (result))
else:
    print("Element is not present in array")