#search for string in txt file
with open("test3.txt","r") as fp:
    f5=fp.read()
    word=input("Enter the string : ")
    for i in f5:
        if word in f5:
            print("Present")
            break
    else:print("Not present")