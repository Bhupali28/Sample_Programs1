#import sys

global sum

def armstrong_num(num):
	sum = 0
	temp = num
	while (temp > 0):
		no = temp % 10
		sum += no ** len(str(num))
		temp /= 10
	print sum
	return sum
	


try:
	no = int(raw_input("enter the number "))
	sum = armstrong_num(no)
except ValueError:
	#print "Oops!",sys.exc_info()[0],"occured."
    	print "Oops!  That was no valid number.  Try again..."    

else:
	if (sum == no):
		print ("The number is Armstrong")
	else:
		print ("The number is not Armstrong")
