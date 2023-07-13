# importing "array" for array operations
from array import*
#import array
# initializes array with signed integers
arr =array('i', [1, 2, -3])
print(type(arr))

# printing original array
print("The new created array is : ", arr)

# using append() to insert new value at end
arr.append(4);
# printing appended array
print("The appended array is : ", arr)

# inserts 5 at 2nd position
arr.insert(2, 5)
# print(arr.buffer_info())

# printing array after insertion
print("The array after insertion is : ", end="")
print(arr)
