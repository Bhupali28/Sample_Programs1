#!/usr/bin/python

# Hangman Game

import random

def pick_word():

	list1 = []

	f = open ("sowpods_dict.txt","r")
	line = f.readline()
	#list1.append(line)

	while line:
		line = line.strip()
		list1.append(line)
		line = f.readline()
#	print list1
	random_word = random.randint(0,len(list1))

	print "random word is : ",list1[random_word]
	
	return list1[random_word]

def Guess_letters (word):
	guess = "_"*len(word)
	word = list(word)	
	guess = list(guess)
	counter = 1
	while True:
		if counter <= 6 :
			letter = raw_input("Guess your letter : ")
			letter = letter.upper()
			counter += 1
			if letter in word:
				if letter in guess:
					print ("letter already guessed")
			
				for i in range (0,len(word)) :
					if word[i] == letter :
						guess[i] = letter
				print guess
	
			else :
				print ("Incorrect letter !")
		
			if '_' not in guess :
				print ''.join(guess)
				print "Congrates ! You won ! "	
				break
			
		if counter > 6 :	
			option = input("Do You want to continue..? if yes press 1 or press 0 : ")
			if option == 1 :
				counter = 1
			#guess = list("_"*len(word))  <-- if user wants to new start...
				print ("Play again")
				#break
			elif option == 0 :
				print ("You Quit the Game!")				
				break




word = pick_word()
print word
Guess_letters (word)		
