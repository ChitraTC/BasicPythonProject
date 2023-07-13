# Python program for implementation of Selection
# Sort


A = [64, 25, 12, 22, 11]

# Traverse through all array elements
for i in range(len(A)):

    # Find the minimum element in remaining unsorted array
    min_val=max(A[i:])
    min_idx =A.index(min_val)

    # Swap the found minimum element withthe first element
    A[i], A[min_idx] = A[min_idx], A[i]

# Driver code to test above
print("Sorted array :",A)


