import queue
L = queue.Queue(maxsize=4)

L.put(5)
L.put(9)
L.put(1)
L.put(7)
print(L)
#print(list(L))
print("Full: ", L.full())
print(L.get())
print(L.get())
print(L.get())
print(L.get())

print("Empty: ", L.empty())
print("Full: ", L.full())