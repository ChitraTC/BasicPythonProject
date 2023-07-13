# Python3 Program for recursive binary search.

# Returns index of x in arr if present, else -1


def binarySearch(arr,key):
	low=0
	high=len(arr)-1


	# Check base case
	while low<=high :
		mid=(low+high)//2
		# If element is present at the middle itself
		if key==arr[mid]:
			return mid

		# If element is larger than mid, then it can only be present in left subarray
		elif key>arr[mid]:
			low=mid+1
		# Else the element can only be present in right subarray
		else:
			high=mid-1


	else:
		# Element is not present in the array
		return -1


# Driver Code
arr = [2, 3, 4, 10, 40]
key = 1

# Function call
result = binarySearch(arr, key)

if result != -1:
	print("Element is present at index % d" % result)
else:
	print("Element is not present in array")
