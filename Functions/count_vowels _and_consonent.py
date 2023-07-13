#Define a function to count vowels and consonent in a word
def fun(w):
    v=c=0
    for i in w:
        if i in ['a','e','i','o''u']:
            c=c+1
        else:v=v+1
    return(c,v)


w=input("Enter a word : ")
v,c=fun(w)
print("There are",v,"vowels","and",c,"consonents in ",w)