#!/usr/bin/python
file_prime = open ("prime.txt","r")
file_happynos = open ("happy_numbers.txt", "r")

file_primeL = []
file_happynosL = []
list3 = []

file_primeL = file_prime.read().split(',')

file_happynosL = file_happynos.read().split(',')


for i in file_primeL:
	if i in file_happynosL:		
		list3.append(i)
print ("common elements between the lists are : ")			
print list3
 
