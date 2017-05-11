#s = raw_input("enter your name ")
#a = input("enter your number ")

#print s + "s number is " + str(a) 



#print str(a) + " is my number"


#num = (raw_input ("enter the number"))

#print len(num)

string = "Hello World! I Like Python"

print string.count("Hello")

print string.upper()
print string.lower(),"\n" ,string[0:7], "\n" , string[-7:-1] ,"\n", len(string)
print string.split(), "\n", string.find("World"), "\n", string.rfind("World")
print string.replace("Like","Love")

#-------------------------------------------------------
import os

retval = os.getcwd()
print "Current working directory %s" % retval

#------------------------------------------------------------


class Restaurant(object):
    bankrupt = False
    def open_branch(self):
        if not self.bankrupt:
            print("branch opened")

x = Restaurant()
x.bankrupt
#print x.bankrupt

#y = Restaurant()
#y.bankrupt = True
#print y.bankrupt

#-----------------------------------------------------------------

import os

retval = os.getcwd()
print "Current working directory %s" % retval

path = "/home/bhupali/practice programs"

os.chdir(path)
retval = os.getcwd()

print "Directory changed successfully %s" % retval

os.mkdir("newFolder")

listOfDirectories=os.listdir(os.getcwd())

print 'Lists : %s' % listOfDirectories

os.rmdir("newFolder")

#--------------------------------------------------------------------

import json
jsonData = '{"name": "Frank", "age": 39}'
jsonToPython = json.loads(jsonData)
print jsonToPython
print jsonToPython['name']

pythonDictionary = {'name':'Bob', 'age':44, 'isEmployed':True}
dictionaryToJson = json.dumps(pythonDictionary)

print dictionaryToJson
