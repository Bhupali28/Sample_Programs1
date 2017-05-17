#!/usr/bin/python

# Guess Letter

print (" Welcome to Hangman!! ")

word = "EVAPORATE"
#print word
guess = "_"*len(word)
#print guess

word = list(word)
guess = list(guess)
counter = 0
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
		option = input("Do You want to continue..? if yes press 1 or press 0")
		if option == 1 :
			counter = 0
			#guess = list("_"*len(word))  <-- if user wants to new start...
			print ("Play again")
			#break
		elif option == 0 :
			print ("You Quit Hangman Game!")				
			break
	
