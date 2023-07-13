# Python3 code to linearly search x in arr[].
# If x is present then return its location,
# otherwise return -1


def search(arr, N, key):

	for i in range(0, N):
		if (arr[i] == key):
			return i
	return -1


# Driver Code
if __name__ == "__main__":
	arr = [2, 3, 4, 10, 40]
	key = 10
	N = len(arr)

	# Function call
	result = search(arr, N, key)
	if(result == -1):
		print("Element is not present in array")
	else:
		print("Element is present at index", result)
