#generate a random color hex,a random alphabetical string,random value between two integers and random multiple of 7 between 0 to 7


import random

print("Generate a random color hex:")
ran=random.randrange(0,16777216)
print(hex(ran))
colour_code='#'+hex(ran)[2:]
print(colour_code)


l="abcdefghi"
str=""
print("Random string generated: ",end="")
for i in l*5:
    str=str+random.choice(l)
print(str)

print("Random value between two integers:",end="")
n=random.randrange(1,10)
print(n)

print("Random multiple of 7 betwee 0 to 70 : ",end="")
n=random.randrange(0,8)
print(n*7)


