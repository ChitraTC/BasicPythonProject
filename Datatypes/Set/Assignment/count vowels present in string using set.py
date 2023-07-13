#1.count vowels present in string using set
str1="luminar"
set1= {'a','e','i','o','u'}
c=0
for i in str1:
    if i in set1:
        c+=1
print("There are",c,"vowels")
