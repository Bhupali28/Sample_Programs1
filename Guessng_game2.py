#!/usr/bin/python

# Guessing Game 2


def search (num):
	f_no = 0
	l_no = 100
	m_no = 50
	counter = 0
	no = int(raw_input ("is your number is " + str(m_no) + "? " + "if same press 0 or if it is heigher press 1  or if it is lower press 2 "))
	while no != 0:
		counter += 1
		if no == 1 :
			f_no = m_no + 1
		elif no == 2 :
			l_no = m_no - 1
		#elif no == 0 :
		m_no = (f_no + l_no)//2
		no = int(raw_input ("is your number is " + str(m_no) + "? " + "if same press 0 or if it is heigher press 1  or if it is lower press 2 "))
	
	print "How many guesses it took to guess the number : %d" %(counter) 		


num = int(raw_input("Enter the number between 0 to 100 : "))
search (num)	

