# NumPy Array Attributes

import numpy as np


a = np.array([[1, 2, 3], [4, 5, 6]])
# It returns the number of axes (dimensions) of the array.
print("Dimension: ", a.ndim)

a = np.array([[1, 2, 3], [4, 5, 6]])
""" It returns a tuple of the dimension of the array, i.e. (n,m),
where n is number of rows and m is the number of columns """
print("Shape: ", a.shape)

a = np.array([[1, 2, 3], [4, 5, 6]])
# It returns the total number of elements of the array.
print("Size: ", a.size)

a = np.array([[1, 2, 3], [4, 5, 6]])
""" It returns an object describing the type of the elements in the array. """
print("Data Type: ", a.dtype)

""" we can explicitly define the data type of a NumPy array """
a = np.array([[1, 2, 3], [4, 5, 6]], dtype=float)
print("Data Type: ", a.dtype)

a = np.array([[1, 2, 3], [4, 5, 6]])
# It returns the size in bytes of each element of the array.
print("Size (in Bytes): ", a.itemsize)

a = np.array([[1, 2, 3], [4, 5, 6]])
# It returns the buffer containing the actual elements of the array.
print("Data (Buffer):", a.data)

a = np.random.random((2, 3))
print("Array: ", a)
# The function will return the sum of all the elements of the ndarray
print("Sum: ", a.sum())

a = np.random.random((2, 3))
print("Array: ", a)
# The function will return the minimum element value from the ndarray
print(a.min())

a = np.random.random((2, 3))
print("Array: ", a)
# The function will return the maximum element value from the ndarray
print(a.max())
