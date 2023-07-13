#5.	Write a python code to remove all the repeating letters from a each words of a given sentence.
#   			i/p:Let’s google the pineapple
#			o/p:Let’s gole the pineal
#str1=input("Enter the string1:")
str1="Let’s google the pineapple"
str2=str3=""
list1=str1.split() #convert string to list
print(list1)
for i in list1:
    str2=""
    for j in i:
        if j in str2:
            pass
        else:
            str2+=j
    str3=str3+str2+" "
print("Edited String is:",str3)


