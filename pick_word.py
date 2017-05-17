#!/usr/bin/python

# Pick Word


import random

#random_word = random.randint(0,len(list1))

list1 = []

f = open ("sowpods_dict.txt","r")
line = f.readline()
#list1.append(line)

while line:
	line = line.strip()
	list1.append(line)
	line = f.readline()
print list1
random_word = random.randint(0,len(list1))

print "random word is : ",list1[random_word]
