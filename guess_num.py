

import random

class Error(Exception):
	pass
class ValueTooSmallError(Error):
	pass
class ValueTooLargeError(Error):
	pass


randNum=random.randint(1,10)
#print randNum

count = 0
while True:
	try:
		num = raw_input("Guess the number between 1 to 10 ")
		
		if num == "exit":
			break
		count += 1	
		num=int(num)
	
		if num < randNum :
			raise ValueTooSmallError
		elif num > randNum :
			raise ValueTooLargeError
		
	except ValueTooSmallError:
		print "You guessed lower number" 
	except ValueTooLargeError:
		print "You guessed higher number"
	except ValueError:
		print 'Please enter valid input!'
	
	else:
		
		print ("You guessed it correct! Congo!")
			
		break

print "You tried it %d times" %count
		
