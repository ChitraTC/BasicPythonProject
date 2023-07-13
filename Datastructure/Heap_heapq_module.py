# The heap functionalities are in the heapq package, so import it
import heapq

# we now initialise a list to be converted to heap
lis = [15, 7, 9, 4, 13]

# converting lis to heap using the heapify function
heapq.heapify(lis)
print("The heap looks like: ")
print(lis)

# using the heappop function
print("The popped item using heappushpop() is : ", end="")
print(heapq.heappop(lis))

print("After popping, the heap looks like: ")
print(lis)

# using the heappush function to push 2
print("After pushing 2, the heap looks like: ")
heapq.heappush(lis, 2)
print(lis)