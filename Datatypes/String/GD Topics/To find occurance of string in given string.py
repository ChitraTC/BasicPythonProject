#s=input("Enter the string:")
s="Welcome to USA.USA is awesome,isn't it?USA is commonly called as united states"
sf="USA"
l=len(sf)
print("input:",s)
ns=ns1=ns2=""
c=0
m=s.find("USA")
c=s.count("USA")
print(sf,"is repeated",c,"times")

print(s.find("USA"))
for i in s[0:l+m]:
    ns=ns+i
print(ns)
if c>=2:
    for i in s[l+m::]:
        ns1=ns1+i
    #print(ns1)
    ns2=ns1.replace("USA","It",c)
    print(ns2)
print("Output:",ns+ns2)










