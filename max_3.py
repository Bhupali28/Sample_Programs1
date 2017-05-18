#!/usr/bin/python
# Max of Three

def max_3(a,b,c):
	largest_no = 0
	if(a>b):
		largest_no = a
		if(a>c):
			largest_no = a
		else : 		
			largest_no = c
	else:	
		if (b>c):
			largest_no = b
		else : 
			largest_no = c
	return largest_no



num1 = input("Enter the 1st number : ")
num2 = input("Enter the 2nd number : ")
num3 = input("Enter the 3rd number : ")

print "largest number from %d , %d and %d is %d" %(num1,num2,num3,max_3(num1,num2,num3))
