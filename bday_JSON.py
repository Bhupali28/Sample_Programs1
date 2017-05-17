#!/usr/bin/python

# Birthday JSON

import json


def dict_read():
	f = open("birthday.json", "r")
	Birthdays = json.load(f)
	#print Birthdays	
	for name in Birthdays:
		print name

def add_name():
	f = open("birthday.json", "r")
	Birthdays = json.load(f)
	name = raw_input ("Who's BDay do you want to add : ")
	print ("Date of %s : " %(name))
	date = raw_input()
	
	Birthdays[name] = date
	print Birthdays

	f1 = open ("birthday.json", "w")
	json.dump(Birthdays,f1)
	print ("Name and Date added to the dictionary ")

def search_name():
	f = open("birthday.json", "r")
	Birthdays = json.load(f)
	name = raw_input ("Who's birthday do you want to look up? ")
	if name in Birthdays:
		print ("%s's birthday is at %s  " %(name,Birthdays[name]))
	else:
		print ("Sorry we don't have %s's Bday in Dictionary " %(name))


while True:
	option = input ("What do you want ? \n 1: Add Name\n 2: Search Name \n 3: Read Dictionary \n 4: Exit ")
	if option == 1 :
		add_name()
		#break
	elif option == 2 :
		search_name()
		#break
	elif option == 3 :
		dict_read()
		#break
	else:
		print("exit")
		break



