#!/usr/bin/python
import random


randNum = '0123456789'

randNum = random.sample(randNum,4)

randnum = int (''.join (random.sample(randNum,4)))
print randnum
cows = 0
bulls = 0
while True:
	print ("Welcome to the Cows and Bulls game")
	num = raw_input("Enter the 4 digit number ")	

		
	if num == 'exit':
		break
		
	num = int(num)

	for i in range(0,4):
		
		no = num % 10
	
		r_no = randnum % 10

		if (no == r_no):
			cows += 1
		elif str(no) in randNum:	
			bulls += 1	
		num = num/10
			
		randnum = randnum/10
		
	print cows,bulls

	
	
