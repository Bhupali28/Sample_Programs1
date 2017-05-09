import os

ftest = open("sample.txt", "r+")

print "The name of the File : ", ftest.name
ftest.write("python is a great language")

ftest.seek(0,0); #Reposition the counter
str = ftest.read(04);
print "read string is : ",str

os.rename("sample.txt","practice.txt")
print "The name of the file :", ftest.name

ftest.close()


