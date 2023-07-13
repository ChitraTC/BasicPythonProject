file1=open("samplefile.txt","w")
file1.write("Have a good day!!")
file1.close

file1=open("samplefile.txt","r")
# print(file1.read())
file1=open("samplefile.txt","a")
file1.write(" Blissfull")
file1.close

file1=open("samplefile.txt","r")
# print(file1.read())
file1.close()
file1=open("Nachu.txt","w")
file1.write("I am Nakshatra\n ")
file1.write("Let the bird of loudest lay,\n""On the sole Arabian tree,\n""Herald sad and trumpet be,\n""To whose sound chaste wings obey.")
#file1=open("samplefile.txt","r")
file1.close()
file1=open("Nachu.txt","r")
print(file1.read(30))
# line=file1.readline()
# print(line[0:6])
