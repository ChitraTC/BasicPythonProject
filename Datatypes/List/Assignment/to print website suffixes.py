#["www.zframez.com", "www.wikipedia.org", "www.asp.net", "www.abcd.in"]
#Write a python program to print website suffixes (com , org , net ,in) from this list.
list1=["www.zframez.com", "www.wikipedia.org", "www.asp.net", "www.abcd.in"]
list2=[]
for i in list1:
    #print(i.removeprefix("www"))
    ldot=i.find(".",5 )#to print whatever elements available after the "."after 3 www we have first dot >hence we have checked from 4th index
    print(i[ldot:])
    list2.append(i[ldot+1      :])
print(list2)




