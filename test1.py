list = [1 , 2 , "Hello" , "World", 2017]     #list examples

print list[3], "\n" , list[1:4], "\n" , list[0]
list[1] = 3;
print list
del list[1];
print list


#------------------------------------------------------------
# Python Tuple

tup = (1,2,3,4,5);
tup1 = (6,);

print tup[2]

print tup * 2

print tup + tup1

if (tup > tup1):
	print ("tup is greater than tup1")
else:
	print ("tup1 is greater than tup")
#--------------------------------------------------------------
# Python Dictionary 

Employee = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}	
print "variable Type: %s" %type (Employee)

#--------------------------------------------------------
# Dictionary

Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}

Boys = {'Tim': 18,'Charlie':12,'Robert':25}

Girls = {'Tiffany':22}

StudentsG = Girls.copy()
print StudentsG

Girls.update ({"Sarah" : 10})
print Girls

del Dict['Tim']
print Dict

print "Length : %d" %len(Boys)

print cmp(Boys,Girls)

Students = Dict.keys()
print Students
Students.sort()

for S in Students:
      print":".join((S,str(Dict[S])))
#-----------------------------------------------
# Logical operators

x = 78
y = 34

print 'y==x is :', y==x
print 'x and y :',x and y

#----------------------------------------------------
# Passed Multiple Arguments and added the values

def addition (*args):
	args = args[0] + args[2] + args[4]
	print args

addition (1,3,5,2,7)

#----------------------------------------------
# Functions Arguments

print x
def multi():
	global x
	
	x = x * 2
	print x
	#return x
	
multi()
print x

