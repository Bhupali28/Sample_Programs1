#!/usr/bin/python

# Birthday Dictionary

Birthdays = {'Bhupali' : '28 July', 'Milind' : '8 April', 'Atharva' : '27 Octobar'}

print ("Welcome to the birthday dictionary. We know the birthdys of :")

for name in Birthdays:
	print name

name = raw_input ("Who's birthday do you want to look up? ")
if name in Birthdays:
	print ("%s's birthday is at %s  " %(name,Birthdays[name]))
else:
	print ("Sorry we don't have %s's Bday in Dictionary " %(name))

