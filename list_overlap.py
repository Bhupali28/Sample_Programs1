# common elements between the list without duplicates

list1 = [0,1,1,4,9,6,12,12,30,47,50,98]
list2 = [1,3,6,8,11,12,20,30,47,65,50,74,86]

list3 = []
for i in list1:
	if (i in list2):
		if (i in list3): continue
		else:		
			list3.append(i)
print ("common elements between the lists")			
print list3	
