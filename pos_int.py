	

try:
	a = int(input("Enter a positive integer: "))
	if a <= 0:
        	raise ValueError
	print a
except (ValueError, NameError) as neg:
	print (type(neg))
	print ("This is not negative number")
	print ("Please enter the valid number")
    	

