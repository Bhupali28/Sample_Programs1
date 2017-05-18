#!/usr/bin/python
# Element search

def search (list1,num):
	#if num in list:
	#	return True
	#else:
	#	return False
	first_index = 0
	last_index = len(list1) - 1
	middle_index=0
	while first_index<=last_index:
		middle_index = (first_index + last_index)//2
		middle_element = list1[middle_index]

		if (middle_element == num):
			return True
		elif (middle_element > num):
			last_index = middle_index-1
		else:	
			first_index = middle_index+1
	
	return False



list1 = [1, 3, 5, 30, 42, 43, 500]
print list1

num = input("Enter the element to be search")

print search (list1,num)
