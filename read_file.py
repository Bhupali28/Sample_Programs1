#!/usr/bin/python

# Reading from file

f = open ("name_list.txt", "r")
f1 = f.readline()
name_list = []
while f1:
	f1 = f1.strip()
	name_list.append(f1)
	f1 = f.readline()
	
print name_list
