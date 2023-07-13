import random
print(dir(random))
list1=[12,3,4,5]
#print(random.choice(list1))
print(random.random())#prints a random num b/w 0 to 1
print(random.randrange(2,6))#prints a random num from 2 to n-1 also increment
print(random.randint(5,15))#prints a random num from 2 to n
random.shuffle(list1)
print(list1)
#print(random.shuffle(list1))  = returns none
