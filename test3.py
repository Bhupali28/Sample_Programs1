import sys
    
try:
    num = int(input("Enter the number: "))
    print "The number is", num
    s = num * num
    print "The square of %d is %d" %(num,s)

except:
    print "Oops!",sys.exc_info()[0],"occured."
    print "Please enter the valid number"       
