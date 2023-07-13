# Python program to demonstrate stack implementation using list

stack = []

# append() function to push element in the stack
stack.append('a')
stack.append('b')
print(stack)
stack.append('c')

print('Initial stack')
print(stack)

# pop() function to pop element from stack in LIFO order
print('\nElements popped from stack:')
print(stack.pop())
print(stack)
print(stack.pop())
print(stack.pop())

print('\nStack after elements are popped:')
print(stack)

# print(stack.pop())
# will cause an IndexError
# as the stack is now empty
