#!/usr/bin/python
import random


randNum = '0123456789'

randNum = list(random.sample(randNum,4))

print randNum
cows = 0
bulls = 0
while True:
	print ("Welcome to the Cows and Bulls game")
	num = raw_input("Enter the 4 digit number ")
	
	if num == 'exit':
		break
		
	num = list (num)
	print num
	for i in range(0,4):
		if num[i] == randNum[i]:
			cows +=1
		elif num[i] in randNum:
			bulls +=1
	print 'cows : ',cows
	print 'bulls : ',bulls
	
	if num == randNum :
		print("Congrates ! You have guessed correct number...")
		break

	

