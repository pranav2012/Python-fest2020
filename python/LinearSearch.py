# main code for linear search
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

# input list
print("Enter the elements:")
A=list(map(int,input().split()))
print("Enter the element to be searched:")
x=int(input())

result = linear_search(A,x)
if result != -1:
    print("Element is present at index", (result))
else:
    print("Element is not present in array")